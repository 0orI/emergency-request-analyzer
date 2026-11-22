days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
requests = [14, 8, 21, 11, 17, 6, 13]
total = 0
max_requests = requests[0]
max_day = days [0]
min_requests = requests[0]
min_day = days [0]
achieved_days = 0
missed_days = 0
high_workload_days = 0
high_workload_requests = 0
for i in range(len(requests)):
    total += requests [i]
    if requests [i] > max_requests:
        max_requests = requests [i]
        max_day = days [i]
    if requests [i] < min_requests:
        min_requests = requests [i]
        min_day = days [i]
    if requests [i] >= 12:
        achieved_days += 1
    else:
        missed_days += 1
    if requests [i] > 15:
            high_workload_requests += requests [i]
            high_workload_days += 1
            print(days[i], requests[i], "requests")
average = total / len(requests)
percentage = achieved_days / len(requests) * 100
weekend_requests = requests [5] + requests [6]
weekend_percentage = weekend_requests / total * 100
weekday_requests = total - weekend_requests
weekday_average = weekday_requests / 5
high_workload_days_percentage = high_workload_days / len(requests) * 100
weekday_percentage = weekday_requests / total *100
high_workload_requests_percentage = high_workload_requests / total * 100
if high_workload_days > 0:
    high_workload_average = high_workload_requests / high_workload_days
else:
    high_workload_average = 0
if weekday_average >= 15 and weekday_requests >= 80:
    workload_status = "Critical workload"
else:
    workload_status = "Normal workload"
print(f"Total amount of requests are {total}")
print(f"Average daily requests are {average:.2f}")
print(f"Maximum amount of requests is {max_requests} in {max_day}")
print(f"Minimum amount of requests is {min_requests} in {min_day}")
print(f"Days with target achieved are {achieved_days}")
print(f"Days with target missed are {missed_days}")
print(f"Target achievment rate is {percentage:.2f}%")
print(f"Weekend amount of requests is {weekend_requests}")
print(f"Percentage of weekend requests is {weekend_percentage:.2f}%")
print(f"Amount of weekday requests is {weekday_requests}")
print(f"Average amount of weekday requests is {weekday_average:.2f}")
print(f"Weekday requests percentage is {weekday_percentage:.2f}%")
print(f"High workload requests: {high_workload_requests}")
print(f"Amount of high workload days is {high_workload_days}")
print(f"High workload days percentage: {high_workload_days_percentage:.2f}%")
print(f"High workload requests percentage: {high_workload_requests_percentage:.2f}%")
print(f"High workload average: {high_workload_average}")
print(f"Workload status: {workload_status}")