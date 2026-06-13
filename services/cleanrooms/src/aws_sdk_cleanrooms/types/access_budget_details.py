"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.access_budget_type
    import aws_sdk_cleanrooms.types.auto_refresh_mode
    import aws_sdk_cleanrooms.types.budget
    import aws_sdk_cleanrooms.types.remaining_budget


class AccessBudgetDetails(TypedDict):
    start_time: "datetime.datetime"
    """<p>The start time for the access budget period.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for the access budget period.</p>"""
    remaining_budget: "aws_sdk_cleanrooms.types.remaining_budget.RemainingBudget"
    """<p>The remaining budget amount available for use within this access budget.</p>"""
    budget: "aws_sdk_cleanrooms.types.budget.Budget"
    """<p>The total budget allocation amount for this access budget.</p>"""
    budget_type: "aws_sdk_cleanrooms.types.access_budget_type.AccessBudgetType"
    """<p>Specifies the time period for limiting table usage in queries and jobs. For calendar-based periods, the budget can renew if auto refresh is enabled. For lifetime budgets, the limit applies to the total usage throughout the collaboration. Valid values are:</p> <p> <code>CALENDAR_DAY</code> - Limit table usage per day.</p> <p> <code>CALENDAR_WEEK</code> - Limit table usage per week.</p> <p> <code>CALENDAR_MONTH</code> - Limit table usage per month.</p> <p> <code>LIFETIME</code> - Limit total table usage for the collaboration duration.</p>"""
    auto_refresh: NotRequired[
        "aws_sdk_cleanrooms.types.auto_refresh_mode.AutoRefreshMode"
    ]
    """<p>Indicates whether the budget automatically refreshes for each time period specified in <code>budgetType</code>. Valid values are:</p> <p> <code>ENABLED</code> - The budget refreshes automatically at the start of each period.</p> <p> <code>DISABLED</code> - The budget must be refreshed manually.</p> <p> <code>NULL</code> - The value is null when <code>budgetType</code> is set to <code>LIFETIME</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetDetails) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["startTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["endTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["remainingBudget"] = value["remaining_budget"]
    out["budget"] = value["budget"]
    import aws_sdk_cleanrooms.types.access_budget_type

    out["budgetType"] = aws_sdk_cleanrooms.types.access_budget_type.serialize_json(
        value["budget_type"]
    )
    if "auto_refresh" in value:
        import aws_sdk_cleanrooms.types.auto_refresh_mode

        out["autoRefresh"] = aws_sdk_cleanrooms.types.auto_refresh_mode.serialize_json(
            value["auto_refresh"]
        )
    return out


def deserialize_json(data: dict) -> AccessBudgetDetails:
    out: AccessBudgetDetails = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("AccessBudgetDetails.start_time required")
    if "endTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["end_time"] = aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if "remainingBudget" in data:
        out["remaining_budget"] = data["remainingBudget"]
    else:
        raise DeserializationError("AccessBudgetDetails.remaining_budget required")
    if "budget" in data:
        out["budget"] = data["budget"]
    else:
        raise DeserializationError("AccessBudgetDetails.budget required")
    if "budgetType" in data:
        import aws_sdk_cleanrooms.types.access_budget_type

        out["budget_type"] = (
            aws_sdk_cleanrooms.types.access_budget_type.deserialize_json(
                data["budgetType"]
            )
        )
    else:
        raise DeserializationError("AccessBudgetDetails.budget_type required")
    if "autoRefresh" in data:
        import aws_sdk_cleanrooms.types.auto_refresh_mode

        out["auto_refresh"] = (
            aws_sdk_cleanrooms.types.auto_refresh_mode.deserialize_json(
                data["autoRefresh"]
            )
        )
    return out
