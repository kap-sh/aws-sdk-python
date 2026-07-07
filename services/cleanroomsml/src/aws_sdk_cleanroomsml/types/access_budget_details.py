"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudgetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.access_budget_type
    import aws_sdk_cleanroomsml.types.auto_refresh_mode
    import aws_sdk_cleanroomsml.types.budget


class AccessBudgetDetails(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time of this budget period.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of this budget period. If not specified, the budget period continues indefinitely.</p>"""
    remaining_budget: "aws_sdk_cleanroomsml.types.budget.Budget"
    """<p>The amount of budget remaining in this period.</p>"""
    budget: "aws_sdk_cleanroomsml.types.budget.Budget"
    """<p>The total budget amount allocated for this period.</p>"""
    budget_type: "aws_sdk_cleanroomsml.types.access_budget_type.AccessBudgetType"
    """<p>The type of budget period. Calendar-based types reset automatically at regular intervals, while LIFETIME budgets never reset.</p>"""
    auto_refresh: NotRequired[
        "aws_sdk_cleanroomsml.types.auto_refresh_mode.AutoRefreshMode"
    ]
    """<p>Specifies whether this budget automatically refreshes when the current period ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetDetails) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["startTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["endTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["remainingBudget"] = value["remaining_budget"]
    out["budget"] = value["budget"]
    import aws_sdk_cleanroomsml.types.access_budget_type

    out["budgetType"] = aws_sdk_cleanroomsml.types.access_budget_type.serialize_json(
        value["budget_type"]
    )
    if "auto_refresh" in value:
        import aws_sdk_cleanroomsml.types.auto_refresh_mode

        out["autoRefresh"] = (
            aws_sdk_cleanroomsml.types.auto_refresh_mode.serialize_json(
                value["auto_refresh"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessBudgetDetails:
    out: AccessBudgetDetails = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("AccessBudgetDetails.start_time required")
    if "endTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
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
        import aws_sdk_cleanroomsml.types.access_budget_type

        out["budget_type"] = (
            aws_sdk_cleanroomsml.types.access_budget_type.deserialize_json(
                data["budgetType"]
            )
        )
    else:
        raise DeserializationError("AccessBudgetDetails.budget_type required")
    if "autoRefresh" in data:
        import aws_sdk_cleanroomsml.types.auto_refresh_mode

        out["auto_refresh"] = (
            aws_sdk_cleanroomsml.types.auto_refresh_mode.deserialize_json(
                data["autoRefresh"]
            )
        )
    return out
