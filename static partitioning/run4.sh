# provide the path of all the trace files
TRACE_DIR1="../utility-based-partitioning" # path of the first trace file (excluding the trace file name)
TRACE_DIR2="../utility-based-partitioning" # path of the second trace file (excluding the trace file name)
TRACE_DIR3="../utility-based-partitioning" # path of the third trace file (excluding the trace file name)
TRACE_DIR4="../utility-based-partitioning" # path of the fourth trace file (excluding the trace file name)
TRACE_DIR5="../utility-based-partitioning" # path of the fifth trace file (excluding the trace file name)
TRACE_DIR6="../utility-based-partitioning" # path of the sixth trace file (excluding the trace file name)

binary=${1}
num1=${2}
num2=${3}
num3=${4}
num4=${5}
num5=${6}
num6=${7}

trace1=`sed -n ''$num1'p' server_workloads.txt | awk '{print $1}'`
trace2=`sed -n ''$num2'p' server_workloads.txt | awk '{print $1}'`
trace3=`sed -n ''$num3'p' server_workloads.txt | awk '{print $1}'`
trace4=`sed -n ''$num4'p' server_workloads.txt | awk '{print $1}'`
trace5=`sed -n ''$num5'p' server_workloads.txt | awk '{print $1}'`
trace6=`sed -n ''$num6'p' server_workloads.txt | awk '{print $1}'`

mkdir -p results # change the name of your folder as required
(${binary} -warmup_instructions 25000000 -simulation_instructions 1000000000 -traces ${TRACE_DIR1}/${trace1} ${TRACE_DIR2}/${trace2} ${TRACE_DIR3}/${trace3} ${TRACE_DIR4}/${trace4} ${TRACE_DIR5}/${trace5} ${TRACE_DIR6}/${trace6}) > results/mix-${num1}-${num2}-${num3}-${num4}-${num5}-${num6}.txt & # change the name of the folder as required