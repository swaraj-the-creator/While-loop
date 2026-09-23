total_chores = 4
orignal_count = total_chores
print("You have {orignal_count} chores to finish today! \n")
completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take uot the trash"
    else: next_chore = "Wash the dishes"
    answer = input("Have you finished : {next_chore}? (yes/no): ")
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great Job! Chore completed.")
    else:
        print("Okay, finish it and check again!")
    print("Chores remaining:",total_chores - completed_count)
    print()
print("===== ALL CHORES COMPLETE =====")
print("Great work finishing your entire checklist today! \n")
print("Now let's safely peek at an inifinite loop. . .")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("Stopping here on purpose - a real infinite loop never stops")
        break
print("\n===== Chore Checklist Summary =====")
print("Chores Assigned Today: ",orignal_count)
print("Chores Completed: ",completed_count)
print("Chores Remaining: ",total_chores - completed_count)
