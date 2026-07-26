"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudgetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.access_budget_type
    import capo_cleanroomsml.types.auto_refresh_mode
    import capo_cleanroomsml.types.budget


class AccessBudgetDetails(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time of this budget period.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of this budget period. If not specified, the budget period continues indefinitely.</p>"""
    remaining_budget: "capo_cleanroomsml.types.budget.Budget"
    """<p>The amount of budget remaining in this period.</p>"""
    budget: "capo_cleanroomsml.types.budget.Budget"
    """<p>The total budget amount allocated for this period.</p>"""
    budget_type: "capo_cleanroomsml.types.access_budget_type.AccessBudgetType"
    """<p>The type of budget period. Calendar-based types reset automatically at regular intervals, while LIFETIME budgets never reset.</p>"""
    auto_refresh: NotRequired[
        "capo_cleanroomsml.types.auto_refresh_mode.AutoRefreshMode"
    ]
    """<p>Specifies whether this budget automatically refreshes when the current period ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetDetails) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["startTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_cleanroomsml.types._prelude.timestamp

        out["endTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["remainingBudget"] = value["remaining_budget"]
    out["budget"] = value["budget"]
    import capo_cleanroomsml.types.access_budget_type

    out["budgetType"] = capo_cleanroomsml.types.access_budget_type.serialize_json(
        value["budget_type"]
    )
    if "auto_refresh" in value:
        import capo_cleanroomsml.types.auto_refresh_mode

        out["autoRefresh"] = capo_cleanroomsml.types.auto_refresh_mode.serialize_json(
            value["auto_refresh"]
        )
    return out


def deserialize_json(data: dict) -> AccessBudgetDetails:
    out: AccessBudgetDetails = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["start_time"] = capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("AccessBudgetDetails.start_time required")
    if "endTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["end_time"] = capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
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
        import capo_cleanroomsml.types.access_budget_type

        out["budget_type"] = (
            capo_cleanroomsml.types.access_budget_type.deserialize_json(
                data["budgetType"]
            )
        )
    else:
        raise DeserializationError("AccessBudgetDetails.budget_type required")
    if "autoRefresh" in data:
        import capo_cleanroomsml.types.auto_refresh_mode

        out["auto_refresh"] = (
            capo_cleanroomsml.types.auto_refresh_mode.deserialize_json(
                data["autoRefresh"]
            )
        )
    return out
