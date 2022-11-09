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

