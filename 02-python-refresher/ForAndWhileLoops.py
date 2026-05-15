my_list = [1,2,3,4,5]

sum_of_for_loop = 0

for i in my_list:
    sum_of_for_loop += i

print(sum_of_for_loop)

my_list2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in my_list2:
    print(f"Happy {i}!")

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now bigger than 5")
