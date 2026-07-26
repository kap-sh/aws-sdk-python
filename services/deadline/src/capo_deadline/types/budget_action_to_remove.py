"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionToRemove``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.budget_action_type
    import capo_deadline.types.threshold_percentage


class BudgetActionToRemove(TypedDict, closed=True):
    type: "capo_deadline.types.budget_action_type.BudgetActionType"
    """<p>The type of budget action to remove.</p>"""
    threshold_percentage: "capo_deadline.types.threshold_percentage.ThresholdPercentage"
    """<p>The percentage threshold for the budget action to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionToRemove) -> dict:
    out: dict = {}
    import capo_deadline.types.budget_action_type

    out["type"] = capo_deadline.types.budget_action_type.serialize_json(value["type"])
    out["thresholdPercentage"] = value["threshold_percentage"]
    return out


def deserialize_json(data: dict) -> BudgetActionToRemove:
    out: BudgetActionToRemove = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_deadline.types.budget_action_type

        out["type"] = capo_deadline.types.budget_action_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("BudgetActionToRemove.type required")
    if "thresholdPercentage" in data:
        out["threshold_percentage"] = data["thresholdPercentage"]
    else:
        raise DeserializationError("BudgetActionToRemove.threshold_percentage required")
    return out
