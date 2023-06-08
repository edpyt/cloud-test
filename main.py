n, t = map(int, input().split())
list_coworkers = tuple(map(int, input().split()))

max_floor, min_floor = list_coworkers[-1], list_coworkers[0]

out_employee = int(input())

x1 = max_floor - min_floor + max_floor - out_employee
x2 = max_floor - min_floor + out_employee - min_floor

print(x1, x2)