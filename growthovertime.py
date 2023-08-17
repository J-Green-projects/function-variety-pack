'''
This function is based on the following non-linear growth problem:
At each time step, one new producer is created. Each producer creates X (user-defined) items per time step.
It can solve how many items will have been cumulatively produced in a user-defined time period, or how long it will take to produce a user-defined number of items, or both.
'''



def count_production(
        time_step, 
        items=1,
        time_units="hours",
        time_limit=float("inf"), 
        item_target=float("inf"),
        arbitrary_iteration_limit=999,
        return_list=True,
        only_display_last_step=True
        ):
    '''
    time_step -> (num)\n
    items -> (num) time_step but for the item value\n
    time_units -> (str) the unit of time. Will be included in the print out if return_list=False\n
    time_limit -> (num) the maximum amount of time-steps taken. Ex. if time_step=1 and time_limit=2, then the loop will run for two passes, but if time_step=0.4, it will run for 5\n
    item_target -> (num) the target number of items. Has the same role as time_limit, but is a minimum value to reach, rather than a cannot exceed value\n
    arbitrary_iteration_limit -> (num) a safety feature to prevent the function from outputting thousands of lines. Can be whatever you want, or disabled by setting to infinity\n
    return_list -> (bool) if True, function returns a list of lists [[time,items],[time+i, items+i]]that can be queried. If False, prints the result of each iteration.\n
    only_display_last_step -> (bool) if True, and return_list=False, only print the last iteration.
    '''
    
    iterator = 0
    item_count = 0
    summary = []


    while (iterator+1)*time_step <= time_limit and item_count <= item_target and iterator < arbitrary_iteration_limit:

        iterator+=1 # advance in time
        current_items = iterator * items 
        current_time = iterator * time_step

        item_count+=current_items
        
        summary.append([current_time, item_count])

    if return_list == False:
        if only_display_last_step == False:
            for i in range(len(summary)):
                print("time: " + str(summary[i][0]) + " " + time_units + "\nitem count: " + str(summary[i][1]) + "\n")
                # time: X hours
                # item count: X
        else:
            print("time: " + str(summary[-1][0]) + " " + time_units + "\nitem count: " + str(summary[-1][1]) + "\n")
        return
    else: 
        return summary



# example use: "how long will it take to produce at least 50 items, cumulatively?"
# count_production(time_step=1, item_target=50, return_list=False, only_display_last_step=False)