# CS773 Project: Low-Leakage Dynamic Partitioning in Branch Target Buffer

## Overview
This project investigates methods to reduce leakage power in branch target buffers (BTBs) using dynamic partitioning. The objective is to enhance energy efficiency and security in modern processors while preserving performance. Additionally, it analyzes and compares the performance and security aspects of the implementation with existing partitioning frameworks : static partitioning and utility based partitioning.


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CS773-Project-Low-Leakage-Dynamic-Partitioning-in-Branch-Target-Buffer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd CS773-Project-Low-Leakage-Dynamic-Partitioning-in-Branch-Target-Buffer
    ```
3. Install the trace files mentioned in workloads.txt .


## Usage
1. Build the simulation:
    ```bash
    ./build-champsim [NUMBER OF TRACE FILES]
    ```
2. Run the simulation:
    ```bash
    ./run[NUMBER OF TRACE FILES].sh [binary] 1 2 3 --
    ```
    Select trace files based on the `workloads.txt`.

## Project Structure
- `baseline/`: Contains source code for simulating multiple trace files on a single CPU.
- `static_partitioning/`: Allocates specific sets to each trace file, restricting access to only those sets.
- `utility_based_partitioning/`: Implements a "fake BTB" to track the utilization of each trace file for different partition sets. 
Dynamically allocates set sizes to maximize hits per trace file. (yet to be done)

## References
1. Untangle: A Principled Framework to Design Low-Leakage, High-Performance Dynamic Partitioning Schemes [https://iacoma.cs.uiuc.edu/iacoma-papers/asplos23.pdf]

2. Utility-based cache partitioning: A low-overhead, high-performance, runtime mechanism to partition shared caches [https://safari.ethz.ch/architecture_seminar/fall2018/lib/exe/fetch.php?media=quereshi-micro2006.pdf]

## Contributors
- Mugdha, Anushka

## Acknowledgments
Special thanks to the CS773 course instructor and TAs for their guidance and support.