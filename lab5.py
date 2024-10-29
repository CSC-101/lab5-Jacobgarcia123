import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1,time2):
    total_seconds = time1.hour * 3600 + time1.minute * 60 + time1.second + \
        time2.hour * 3600 + time2.minute * 60 + time2.second
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds // 60) % 60
    seconds = (total_seconds % 60)
    return (hours,minutes,seconds)



# Part 4
def is_descending(numbers:list[float]) -> bool:
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers [i - 1]:
            return False
    return True




# Part 5
def largest_between(numbers:list[int],lower:int,upper:int):
    if lower > upper:
        return None
    lwb = max(0,lower) #lower within bounds
    uwb = min(len(numbers) - 1, upper) #upper within bounds
    if lwb > uwb:
        return None
    maxim = lwb
    for i in range(lwb,uwb + 1):
        if numbers[i] > numbers[maxim]:
            maxim = i
    return maxim





# Part 6
def furthest_from_origin(points: list)->list[int]:
    if not points:
        return None
    maxim = 0
    maxim_distance = points[0].x ** 2 + points[0].y ** 2

    for i in range(1,len(points)):
        distance = points[i].x ** 2 + points[i].y ** 2
        if distance > maxim_distance:
            maxim_distance = distance
            maxim = i
    return maxim