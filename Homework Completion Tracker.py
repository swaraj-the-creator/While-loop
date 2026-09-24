total_homework = 3
orignal_count = total_homework
print("You have ",orignal_count," chores to finish today! \n")
completed_count = 0
homework_num = 1
while homework_num <= total_homework:
    if homework_num == 1: next_ho = "Maths Page 34"
    elif homework_num == 2: next_ho = "SST Page 67"
    else: next_ho = "Science Page 19"
    answer = input("Have you finished your homework? (yes/no): ")
    if answer == "yes":
        completed_count += 1
        homework_num += 1
        print("Great Job! Homework completed.")
    else:
        print("Okay, finish it and check it again!")
    print("Homeworks remaining:",total_homework - completed_count)
    print()
print("============  ALL HOMEWORKS COMPLETE ============")
print("Great work finishing your entire homeworks today!")
print("=================================================")        
