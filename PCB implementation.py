def interrupt_execution(processes, current_time, process_states, running_process_index):
    if running_process_index != -1:
        print("Automatic interrupt at time {}".format(current_time))
    
        process_states[running_process_index] = "stopped"
        running_process_index = -1

    return current_time, process_states, running_process_index

def print_process_state(processes, current_time, process_states):
    print("-----------------")
    for i, state in enumerate(process_states):
        print("|P{} is {}|".format(i + 1, state))
    print("-----------------")



n = int(input("Enter The No. Of Processes (MAX 5): "))
quant = int(input("Enter The Quantum (MAX 3): "))

p = []

for i in range(n):
    p.append({
        'pos': i + 1,
        'AT': 0,
        'BT': 0,
        'ST': [0] * 20,
        'WT': 0,
        'FT': 0,
        'TAT': 0,
        'IS': [[] for _ in range(n)]  # Create n empty lists for 'IS' key
    })


print("Enter Arrival Time of Processes:")
for i in range(n):
    p[i]['AT'] = int(input(f"Arrival Time For Process P{i+1} = "))

ins=[]*n
print("Enter Burst Time Of Processes (MAX 10):")
for i in range(n):
    burst_time = int(input(f"Burst time of process P{i+1} = "))
    p[i]['BT'] = burst_time  # Assign burst time to the corresponding dictionary
    ins.append(burst_time)   # Append burst time to the 'ins' list

for i in range (n):
    for j in range(ins[i]):
        p[i]["IS"][i].append("I" + str(i+1) + str(j))


c = n
s = [[-1] * 20 for _ in range(n)]
time = 0
mini = float('inf')
b = [0] * n
a = [0] * n

for i in range(n):
    b[i] = p[i]['BT']
    a[i] = p[i]['AT']

tot_wt = 0
tot_tat = 0

process_states = ["Not Started"] * n

response_times = [-1] * n  # Initialize response_times array

print(" ==================================================== OUTPUT ==============================================")


print("Scheduling Algo: Round Robin")
print("-----------------------------------------------")
print("Burst time: ", end="")
for i in range(n):
            print(f" P{i+1}: {ins[i]}min,", end="")
print(f"", end="\n")
print("-----------------------------------------------")
print(f"Quantum size: {quant}min", end="\n")
print("-----------------------------------------------")
print("Arrival time: ", end="")
for i in range(n):
                print(f" P{i+1}: {p[i]['AT']}min,", end="")
print("", end="\n")
print("-----------------------------------------------")
for i in range(n):
    instruction_list = p[i]["IS"][i]  # Get the inner array for the current process
    print(f"Instructions For Process P{i+1}: {instruction_list}")
print("-----------------------------------------------")
print("Remaining Execution time: ", end="")
for i in range(n):
        print(f" P{i+1}: {b[i]}min,", end="")
print("", end="\n")
print("-----------------------------------------------")
   


running_process_index = -1  # Initialize to -1 (no running process)


while c != 0:
    mini = float('inf')
    flag = False

    for i in range(n):
        p_val = time + 0.1
        if a[i] <= p_val and mini > a[i] and b[i] > 0:
            index = i
            mini = a[i]
            flag = True

    if not flag:
        time += 1
        continue

    if running_process_index != index:
        if running_process_index != -1:
            if b[running_process_index] > 0:
                process_states[running_process_index] = "Waiting"
            else:
                process_states[running_process_index] = "Finished"
        if response_times[index] == -1:
            response_times[index] = time - p[index]['AT']
        running_process_index = index
   
    j = 0
    while s[index][j] != -1:
        j += 1

    if s[index][j] == -1:
        s[index][j] = time
        p[index]['ST'][j] = time

 # Print burst time, arrival time, and quantum size information
   
    print(" ==================================================== At Time {} ==============================================".format(time))
    print(" ================================================= PCB FOR PROCESS {} =========================================".format(index + 1))
    print("Scheduling Algo: Round Robin")
    print("-----------------------------------------------")
    print("Burst time: ", end="")
    print(f" {p[index]['BT']}min", end="")
    print("", end="\n")

    print("-----------------------------------------------")
    print(f"Quantum size: {quant}min", end="\n")
    print("-----------------------------------------------")
    print("Arrival time: ", end="")
    print(f"  {p[index]['AT']}min", end="")
    print("", end="\n")
    print("-----------------------------------------------")
    print("Remaining Execution time: ", end="")
    print(f"  {b[index]}min", end="")
    
    print("", end="\n")
    print("-----------------------------------------------")
   
    if b[index] <= quant:
        # print_process_state(p, time, process_states)
        print("Process P{} running".format(index + 1))  # Print start time when the process resumes  
        print("-----------------------------------------------")
        print("IR: {}".format(p[index]["IS"][index][0]))  # 
        print("-----------------------------------------------")
        
        try:
            if len(p[index]["IS"][index]) == 1 and index < len(p) - 1:
                print("PC: {}".format(p[index+1]["IS"][index+1][0])) 
            elif index == len(p) - 1 and len(p[index]["IS"][index]) == 1  :
                print("PC: NULL")
            else:     
                print("PC: {}".format(p[index]["IS"][index][1]))       
        except IndexError:
              print("PC: NULL")
        print("-----------------------------------------------")

        if p[index]["IS"][index]:
            p[index]["IS"][index].pop(0)
        if p[index]["IS"][index] and quant !=1:
            p[index]["IS"][index].pop(0)
        instruction_list = p[index]["IS"][index]  # Get the inner array for the current process
        print(f"Remaining Instructions for Process P{i+1}: {instruction_list}")
        print("-----------------------------------------------")


        if len(p[index]["IS"][index]) == 1:
            p[index]["IS"][index].pop(0)
        print("Process P{} resume instruction: {}".format(index + 1,"NULL"))  # Print start time when the process resumes  
        print("-----------------------------------------------")
        time += b[index]
        p[index]['FT'] = time
        b[index] = 0
        process_states[index] = "finished"
        c -= 1
    else:
        # print_process_state(p, time, process_states)
        print("Process P{} running".format(index + 1))  # Print start time when the process resumes  
        print("-----------------------------------------------")
        print("IR: {}".format(p[index]["IS"][index][0]))
        print("-----------------------------------------------")
        try:
            if len(p[index]["IS"][index]) == 1 and index < len(p) - 1:
                print("PC: {}".format(p[index+1]["IS"][index+1][0])) 
            elif index == len(p) - 1 and len(p[index]["IS"][index]) == 1  :
                print("PC: NULL")
            else:     
                print("PC: {}".format(p[index]["IS"][index][1]))       
        except IndexError:
              print("PC: NULL")
        print("-----------------------------------------------")
            
        if p[index]["IS"][index]:
            p[index]["IS"][index].pop(0)
        if p[index]["IS"][index] and quant !=1:
            p[index]["IS"][index].pop(0)
        
        if quant ==3 :
            print("Process P{} resume instruction: {}".format(index + 1,p[index]["IS"][index][1] ))  # Print start time when the process resumes  
        else:
            print("Process P{} resume instruction: {}".format(index + 1,p[index]["IS"][index][0] ))  # Print start time when the process resumes 
        
        print("-----------------------------------------------")
        instruction_list = p[index]["IS"][index]  # Get the inner array for the current process
        print(f"Remaining Instructions: {instruction_list}")
        print("-----------------------------------------------")

        if len(p[index]["IS"][index]) >= 1 and quant==3:
            p[index]["IS"][index].pop(0)

        time += quant
        b[index] -= quant
        process_states[index] = "running"

    if time == 5 or time == 6:
        time, process_states, running_process_index,  = interrupt_execution(p, time, process_states, running_process_index, )

    if b[index] > 0:
        a[index] = time + 0.1

    if b[index] == 0:
        p[index]['WT'] = p[index]['FT'] - p[index]['AT'] - p[index]['BT']
        tot_wt += p[index]['WT']
        p[index]['TAT'] = p[index]['BT'] + p[index]['WT']
        tot_tat += p[index]['TAT']
        process_states[index] = "finished"
    print_process_state(p, time, process_states)
    


avg_wt = tot_wt / float(n)
avg_tat = tot_tat / float(n)
avg_response_time = sum(response_times) / float(n)


total_burst_time = sum(p[i]['BT'] for i in range(n))
utilization_time = total_burst_time / sum(p[i]['TAT'] for i in range(n))

# Print individual process metrics table
print("\nIndividual Process Metrics:")
print("--------------------------------------------------------------------------------------------------------------------------")
print("| Processes | Arrival time | Burst time | Wait time | Response time | Turnaround time | Completion time |    Start time  |")
print("--------------------------------------------------------------------------------------------------------------------------")
for i in range(n):
    first_start_time = p[i]['ST'][0] if p[i]['ST'][0] != 0 else p[i]['AT']
    response_time = first_start_time - p[i]['AT']
    
    # Calculate the start time
    start_time = first_start_time if process_states[i] != "waiting" else "-"
    
    print("|   P{:d}      |     {:3d}      |    {:3d}     |   {:3d}     |       {:3d}     |      {:3d}        |      {:3d}        |      {:3}        |".format(
        i + 1, p[i]['AT'], p[i]['BT'], p[i]['WT'], response_times[i], p[i]['TAT'], p[i]['FT'], start_time))
print("--------------------------------------------------------------------------------------------------------------------------")


print("\nAverage timings of Round Robin Scheduling process:-")
print("The average Wait time is:", avg_wt)
print("The average TurnAround time is:", avg_tat)
print("The average Response time is:", avg_response_time)
print("The Utilization time of processes in Round Robin Scheduling Algo:", utilization_time)
