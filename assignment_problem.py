from ortools.sat.python import cp_model


def main():
    # This program tries to find an optimal assignment of employees to shifts
    # (3 shifts per day, for 7 days), subject to following constraints:

    # Each employee can request to be assigned to specific shifts.
    # Each employee has a rank. Requests of employees with higher ranks are prioritized.
    # Each employee can choose how many shifts they'd like to work on a particular day.
    # Non-consecutive shifts are not allowed.
    # The optimal assignment maximizes the number of fulfilled shift requests for those with a higher rank.

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    num_employees = 5
    num_shifts = 3
    num_days = 7
    all_employees = range(num_employees)
    all_shifts = range(num_shifts)
    all_days = range(num_days)
    employees_per_shift = [1, 2, 1]  # employees_per_shift[i] indicates number of employees required for shift i
    num_shifts = sum(employees_per_shift)
    # shifts_per_employee [i][j] indicates how many shifts employee i wants to work on day j
    shifts_per_employee = [[2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1],
                           [2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 1, 1, 1, 1]]
    priorities = [100, 100, 10, 9, 10]  # priorities[i] indicates rank of employee i
    # shift_requests[i][j][k] indicates whether employee i wants to work shift k on day j
    shift_requests = [[[0, 1, 1], [0, 1, 1], [0, 0, 0], [0, 0, 0], [0, 0, 1],
                       [0, 1, 0], [0, 0, 1]],
                      [[1, 1, 0], [1, 1, 0], [0, 1, 1], [0, 1, 0], [1, 0, 0],
                       [0, 0, 0], [0, 0, 1]],
                      [[0, 1, 0], [0, 1, 0], [0, 0, 0], [1, 0, 0], [0, 0, 0],
                       [0, 1, 0], [0, 0, 0]],
                      [[0, 1, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0],
                       [1, 0, 0], [0, 0, 0]],
                      [[0, 0, 0], [0, 1, 1], [1, 1, 0], [0, 0, 0], [1, 0, 0],
                       [0, 1, 0], [0, 0, 0]]]
     # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: employee 'n' works shift 's' on day 'd'.
    shifts = {}
    for n in all_employees:
        for d in all_days:
            for s in all_shifts:
                shifts[(n, d, s)] = model.NewBoolVar(f'shifts[({n},{d},{s})]')

    # This constraint ensures that each shift has a required number of employees
    # x[s] variable indicates how many employees work in shift s
    x = {}
    for s in all_shifts:
        x[s] = model.NewIntVar(1, 15, f'x[{s}]')

    for s in all_shifts:
        model.Add(x[s] == employees_per_shift[s])

    for s in all_shifts:
        for d in all_days:
            for n in all_employees:
                model.Add(x[s] == sum(shifts[(n, d, s)] for n in all_employees))

    # This constraint ensures that each employee works at max requested number of shifts on a particular day
    # y[(n,d)] indicates how many non-consecutive shifts employee n wants to work on day d
    y = {}
    for n in all_employees:
        for d in all_days:
            y[(n, d)] = model.NewIntVar(1, shifts_per_employee[n][d], f'y[{n}]')

    for n in all_employees:
        for d in all_days:
            for s in all_shifts:
                model.Add(y[(n, d)] >= sum(shifts[(n, d, s)] for s in all_shifts))
   
    # This constraint ensures that no employee works non-consecutive shifts.
    allowed_assignments = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [0, 1, 1]]
    for n in all_employees:
        for d in all_days:
            model.AddAllowedAssignments(
                [shifts[(n, d, s)] for s in all_shifts], allowed_assignments)
                

