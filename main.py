import time

from probe import get_rtt
from udp_probe import udp_probe
from tcp_probe import tcp_probe

from features import extract_features
from svm_model import detect_congestion

from adaptive_probe import adaptive_probe_rate
from traffic_control import throttle_traffic

from filter import moving_average
from predictor import predict_congestion

from throughput import measure_throughput
from logger import log_data

# target hosts (general network monitoring)
targets = [
    "8.8.8.8",
    "1.1.1.1",
    "9.9.9.9"
]


probe_interval = 2
sending_rate = 1


while True:

    print("\n========= Monitoring Cycle =========")

    for host in targets:

        print("\nTarget:", host)

        rtts = []

        # collect RTT samples
        for i in range(5):

            icmp_rtt = get_rtt(host)
            udp_rtt = udp_probe(host)
            tcp_rtt = tcp_probe(host)

            print("ICMP RTT:", icmp_rtt)
            print("UDP RTT:", udp_rtt)
            print("TCP RTT:", tcp_rtt)

            # choose available RTT
            rtt = icmp_rtt or udp_rtt or tcp_rtt

            if rtt:
                rtts.append(rtt)

            time.sleep(probe_interval)

        if len(rtts) == 0:
            print("No RTT samples collected")
            continue

        # smooth RTT values
        rtts = moving_average(rtts)

        print("All RTT samples:", rtts)

        # extract features
        mean_rtt, std_dev, elevation = extract_features(rtts)

        print("Mean RTT:", mean_rtt)
        print("Std Dev:", std_dev)
        print("Latency Elevation:", elevation)

        # SVM detection
        state = detect_congestion(mean_rtt, std_dev, elevation)

        if state == 1:
            print("Network State: CONGESTED")
            congested = True
        else:
            print("Network State: NORMAL")
            congested = False

        # congestion prediction
        if predict_congestion(rtts):
            print("⚠ Congestion trend detected")

        # measure throughput
        throughput = measure_throughput()

        print("Throughput:", throughput, "Mbps")

        # save log
        log_data(mean_rtt, std_dev, elevation, state, throughput)

        # adaptive probe rate
        probe_interval = adaptive_probe_rate(congested, probe_interval)

        # traffic throttling simulation
        sending_rate = throttle_traffic(sending_rate, congested)

        print("Probe interval:", probe_interval)
        print("Sending rate:", sending_rate)

    print("\n--------------------------------------")