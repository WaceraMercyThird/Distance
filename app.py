






speed = float(input("Enter the speed of vehicle in mph: "))
time = int(input("Enter the time vehicle has traveled: "))

print("hour \tDistace Travelled")

for x in range(1, time + 1):
    distance =speed * x
    print(x, "\t", format(distance, '.0f') , sep ="")