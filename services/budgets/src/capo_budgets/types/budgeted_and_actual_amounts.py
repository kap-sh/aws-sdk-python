"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetedAndActualAmounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.spend
    import capo_budgets.types.time_period


class BudgetedAndActualAmounts(TypedDict, closed=True):
    budgeted_amount: NotRequired["capo_budgets.types.spend.Spend"]
    """<p>The amount of cost or usage that you created the budget for.</p>"""
    actual_amount: NotRequired["capo_budgets.types.spend.Spend"]
    """<p>Your actual costs or usage for a budget period.</p>"""
    time_period: NotRequired["capo_budgets.types.time_period.TimePeriod"]
    """<p>The time period that's covered by this budget comparison.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetedAndActualAmounts) -> dict:
    out: dict = {}
    if "budgeted_amount" in value:
        import capo_budgets.types.spend

        out["BudgetedAmount"] = capo_budgets.types.spend.serialize_aws_json_1_1(
            value["budgeted_amount"]
        )
    if "actual_amount" in value:
        import capo_budgets.types.spend

        out["ActualAmount"] = capo_budgets.types.spend.serialize_aws_json_1_1(
            value["actual_amount"]
        )
    if "time_period" in value:
        import capo_budgets.types.time_period

        out["TimePeriod"] = capo_budgets.types.time_period.serialize_aws_json_1_1(
            value["time_period"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BudgetedAndActualAmounts:
    out: BudgetedAndActualAmounts = {}  # type: ignore[typeddict-item]
    if "BudgetedAmount" in data:
        import capo_budgets.types.spend

        out["budgeted_amount"] = capo_budgets.types.spend.deserialize_aws_json_1_1(
            data["BudgetedAmount"]
        )
    if "ActualAmount" in data:
        import capo_budgets.types.spend

        out["actual_amount"] = capo_budgets.types.spend.deserialize_aws_json_1_1(
            data["ActualAmount"]
        )
    if "TimePeriod" in data:
        import capo_budgets.types.time_period

        out["time_period"] = capo_budgets.types.time_period.deserialize_aws_json_1_1(
            data["TimePeriod"]
        )
    return out
