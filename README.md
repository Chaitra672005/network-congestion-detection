# 🚦 Real-Time Network Congestion Detection & Prevention System

## 📌 Overview
This project presents a real-time network congestion detection and prevention system that leverages lightweight probing techniques and machine learning to monitor, analyze, and optimize network performance.

---

## 🚀 Key Features
- RTT-based congestion detection using ICMP, TCP, and UDP probes  
- Machine Learning model (SVM) for congestion classification  
- Adaptive traffic control to reduce latency and improve throughput  
- Real-time monitoring and analysis of network conditions  

---

## 🧠 System Architecture
1. Probe packets are sent across the network to measure Round Trip Time (RTT)  
2. Statistical features are extracted from collected network data  
3. A trained SVM model classifies congestion levels  
4. Adaptive mechanisms adjust traffic flow to mitigate congestion  

---

## 🛠️ Technologies Used
- Python  
- Socket Programming  
- Scikit-learn (SVM)  

---

## 🔍 Testing & Analysis Tools
- Wireshark — packet capture and protocol-level traffic analysis  
- iperf — network performance measurement and throughput testing  

---

## ⚙️ Implementation Details
- Developed lightweight probing mechanism for real-time RTT measurement  
- Implemented feature extraction for network performance metrics  
- Integrated SVM classifier for accurate congestion detection  
- Designed adaptive logic to optimize traffic behavior  

---

## 📊 Results
- Improved network throughput under congestion scenarios  
- Reduced packet delay and response time  
- Reliable classification of congestion states  

