import subprocess
import re

def measure_throughput(server="10.45.111.181"):
    try:
        result = subprocess.run(
            [
                r"C:\Users\B Chaitrashree\Downloads\iperf3.1.4_64\iperf3.exe",
                "-c", server,
                "-t", "3"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr
        print("DEBUG:", output)

        match = re.search(r"(\d+\.?\d*)\s+(Mbits/sec|Gbits/sec)", output)

        if match:
            value = float(match.group(1))
            unit = match.group(2)

            if unit == "Gbits/sec":
                value *= 1000

            return value

        return None

    except Exception as e:
        print("ERROR:", e)
        return None