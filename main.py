def solve_activity_selection(activities):
    """
    Solves the Activity Selection Problem using a greedy approach.
    This function demonstrates a structured problem-solving process:
    1. Problem Definition: Maximize non-overlapping activities.
    2. Data Representation: Activities as (start_time, end_time, name) tuples.
    3. Strategy (Greedy): Sort by finish times, then pick the earliest finishing
       activity that doesn't overlap with the last selected one.
    """
    # 1. Understanding the problem: We need to select activities such that
    #    no two selected activities overlap, and the total number of selected
    #    activities is maximized. This defines our objective and constraints.

    # 2. Breaking down the problem: A common strategy for this type of problem
    #    is to sort the activities by a key that helps make optimal local choices.
    #    For activity selection, sorting by finish time is a proven greedy strategy.
    #    This step is crucial for transforming a complex decision into simpler, sequential ones.
    activities.sort(key=lambda x: x[1]) # Sort activities by their finish times

    selected_activities = []
    last_finish_time = -1 # Initialize with a time before any possible start time

    print("--- Problem: Maximize non-overlapping activities ---")
    print(f"Available activities (start, end, name): {[(a[0], a[1], a[2]) for a in activities]}")
    print("\n--- Solving Process (Iterative Decision Making) ---")

    for i, activity in enumerate(activities):
        start_time, finish_time, name = activity
        # 3. Decision Making (Greedy Choice): If the current activity's start time
        #    is after or at the same time as the last selected activity's finish time,
        #    we can select it. This is our "solution step" for each sub-problem,
        #    making a locally optimal choice that leads to a global optimum.
        if start_time >= last_finish_time:
            print(f"Step {i+1}: Considering activity '{name}' (starts {start_time}, ends {finish_time}).")
            print(f"  Last selected activity finished at {last_finish_time}. '{name}' starts at {start_time}.")
            selected_activities.append(activity)
            last_finish_time = finish_time
            print(f"  -> Selected '{name}'. New last finish time: {last_finish_time}.")
        else:
            print(f"Step {i+1}: Considering activity '{name}' (starts {start_time}, ends {finish_time}).")
            print(f"  Last selected activity finished at {last_finish_time}. '{name}' starts at {start_time}.")
            print(f"  -> Cannot select '{name}' as it overlaps with the previously selected activity.")

    print("\n--- Solution ---")
    return selected_activities

if __name__ == "__main__":
    # Example activities: (start_time, end_time, name)
    # This represents the "initial problem state" or "requirements" that need a solution.
    example_activities = [
        (1, 4, "Meeting A"),
        (3, 5, "Meeting B"),
        (0, 6, "Meeting C"),
        (5, 7, "Meeting D"),
        (3, 9, "Meeting E"),
        (5, 9, "Meeting F"),
        (6, 10, "Meeting G"),
        (8, 11, "Meeting H"),
        (8, 12, "Meeting I"),
        (2, 13, "Meeting J"),
        (12, 14, "Meeting K")
    ]

    # The result of applying the engineering problem-solving approach.
    optimal_schedule = solve_activity_selection(example_activities)

    print("\nFinal Optimal Schedule:")
    if optimal_schedule:
        for activity in optimal_schedule:
            print(f"- {activity[2]} (Starts: {activity[0]}, Ends: {activity[1]})")
    else:
        print("No activities could be scheduled.")
