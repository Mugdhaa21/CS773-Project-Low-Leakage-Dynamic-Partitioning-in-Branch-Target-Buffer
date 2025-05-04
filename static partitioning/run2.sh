# provide the path of all the trace files
TRACE_DIR1="../utility-based-partitioning" # path of the first trace file (excluding the trace file name)
TRACE_DIR2="../utility-based-partitioning" # path of the second trace file (excluding the trace file name)
TRACE_DIR3="."  # path of the third trace file (excluding the trace file name)
TRACE_DIR4="."  # path of the fourth trace file (excluding the trace file name)
binary=${1}
num1=${2}
num2=${3}


trace1=`sed -n ''$num1'p' server_workloads.txt | awk '{print $1}'`
trace2=`sed -n ''$num2'p' server_workloads.txt | awk '{print $1}'`

mkdir -p results # change the name of your folder as required
(${binary} -warmup_instructions 25000000 -simulation_instructions 100000000 -traces ${TRACE_DIR1}/${trace1} ${TRACE_DIR2}/${trace2}) > results/mix-${num1}-${num2}.txt & # change the name of the folder as required