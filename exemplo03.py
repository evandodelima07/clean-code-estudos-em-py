WORK_DAYS_PER_WEEK = 5

real_days_per_ideal_day = 4
sum_weeks = 0

task_estimates = [1, 2, 3] 

for estimate in task_estimates:
    real_task_days = estimate * real_days_per_ideal_day
    real_task_weeks = real_task_days / WORK_DAYS_PER_WEEK
    sum_weeks += real_task_weeks

print(f"Total de semanas: {sum_weeks}")