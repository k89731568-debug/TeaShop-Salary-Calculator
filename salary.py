from constants import *


def is_full_attendance(required_hours, total_hours):

    return total_hours >= required_hours


def calculate_base_salary(role, required_hours, total_hours):

    if total_hours >= required_hours:
        return BASIC_SALARY[role]

    return round(BASIC_SALARY[role] / required_hours * total_hours)


def calculate_performance_pay(role,performance,required_hours,total_hours,):
    multiplier = PERFORMANCE_MULTIPLIER[role]

    if total_hours >= required_hours:
        return multiplier * performance

    return round(multiplier * performance / required_hours * total_hours)
def calculate_regular_overtime( role,required_hours,total_hours,):

    if total_hours < required_hours:
        return 0

    overtime = total_hours - required_hours

    pay = (BASIC_SALARY_NO_OT[role]/ 176* 1.5* overtime)

    return round(pay)
def calculate_holiday_overtime(role,double_ot,triple_ot,):

    double_pay = (BASIC_SALARY_NO_OT[role]/ 176* double_ot)

    triple_pay = (BASIC_SALARY_NO_OT[role]/ 176* 2* triple_ot)

    return round(double_pay + triple_pay)
def calculate_allowance(amount, required_hours, total_hours):

    if total_hours >= required_hours:
        return amount

    return round(amount / required_hours * total_hours)


def calculate_salary(role,required_hours,performance,total_hours,double_ot,triple_ot,):
    result = {}

    result["Base Salary"] = calculate_base_salary(role,required_hours,total_hours,)

    result["Performance Pay"] = calculate_performance_pay(role,performance,required_hours,total_hours,)

    result["Regular Overtime"] = calculate_regular_overtime(role,required_hours,total_hours,)

    result["Holiday Overtime"] = calculate_holiday_overtime(role,double_ot,triple_ot,)

    result["Housing Allowance"] = calculate_allowance(HOUSING_ALLOWANCE[role],required_hours,total_hours,)

    result["Meal Allowance"] = calculate_allowance(MEAL_ALLOWANCE[role],required_hours,total_hours,)

    result["Social Security Allowance"] = calculate_allowance(SOCIAL_SECURITY_ALLOWANCE[role],required_hours,total_hours,)

    result["Full Attendance Bonus"] = calculate_allowance(FULL_ATTENDANCE_BONUS[role],required_hours,total_hours,)

    result["QSC Bonus"] = calculate_allowance(QSC_BONUS[role],required_hours,total_hours,)

    result["Management Allowance"] = calculate_allowance(MANAGEMENT_ALLOWANCE[role],required_hours,total_hours,)

    if role == REGIONAL_MANAGER:
        result["Transportation Allowance"] = calculate_allowance(TRANSPORTATION_ALLOWANCE[role],required_hours,total_hours,)

    return result