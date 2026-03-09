# M/M/1 Queue Simulation for 20 Students in R

lambda <- 4   # arrival rate per hour
mu <- 6       # service rate per hour
n <- 20       # n0 of students

set.seed(42)  


inter_arrival <- rexp(n, rate = lambda)
service <- rexp(n, rate = mu)


arrival <- cumsum(inter_arrival)


start <- numeric(n)
completion <- numeric(n)
wait <- numeric(n)
time_in_sys <- numeric(n)


start[1] <- arrival[1]
completion[1] <- start[1] + service[1]
wait[1] <- 0
time_in_sys[1] <- service[1]


for (i in 2:n) {
  start[i] <- max(arrival[i], completion[i-1])
  completion[i] <- start[i] + service[i]
  wait[i] <- start[i] - arrival[i]
  time_in_sys[i] <- completion[i] - arrival[i]
}


df <- data.frame(
  Student = 1:n,
  Interarrival_hr = inter_arrival,
  Arrival_hr = arrival,
  Service_hr = service,
  Start_hr = start,
  Completion_hr = completion,
  Wait_hr = wait,
  Time_in_sys_hr = time_in_sys
)


print(round(df, 4))


avg_wait <- mean(wait)
avg_time_sys <- mean(time_in_sys)

cat("\n--- Simulation Results ---\n")
cat(sprintf("Average waiting time (simulated): %.4f hours (%.2f minutes)\n", 
            avg_wait, avg_wait * 60))
cat(sprintf("Average time in system (simulated): %.4f hours (%.2f minutes)\n", 
            avg_time_sys, avg_time_sys * 60))


Wq_theoretical <- 1/3   # 20 minutes in hours
Ws_theoretical <- 0.5   # 30 minutes in hours

cat("\n--- Theoretical Values (M/M/1) ---\n")
cat(sprintf("Theoretical average waiting time (Wq): %.4f hours (20.00 minutes)\n", Wq_theoretical))
cat(sprintf("Theoretical average time in system (Ws): %.4f hours (30.00 minutes)\n", Ws_theoretical))

# Differences
cat("\n--- Differences ---\n")
cat(sprintf("Waiting time difference: %.2f minutes\n", abs(avg_wait - Wq_theoretical) * 60))
cat(sprintf("Time in system difference: %.2f minutes\n", abs(avg_time_sys - Ws_theoretical) * 60))