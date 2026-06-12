"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionToAdd``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_action_type
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.threshold_percentage


class BudgetActionToAdd(TypedDict):
    type: "aws_sdk_deadline.types.budget_action_type.BudgetActionType"
    """<p>The type of budget action to add.</p>"""
    threshold_percentage: (
        "aws_sdk_deadline.types.threshold_percentage.ThresholdPercentage"
    )
    """<p>The percentage threshold for the budget action to add.</p>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>A description for the budget action to add.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionToAdd) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.budget_action_type

    out["type"] = aws_sdk_deadline.types.budget_action_type.serialize_json(
        value["type"]
    )
    out["thresholdPercentage"] = value["threshold_percentage"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BudgetActionToAdd:
    out: BudgetActionToAdd = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_deadline.types.budget_action_type

        out["type"] = aws_sdk_deadline.types.budget_action_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("BudgetActionToAdd.type required")
    if "thresholdPercentage" in data:
        out["threshold_percentage"] = data["thresholdPercentage"]
    else:
        raise DeserializationError("BudgetActionToAdd.threshold_percentage required")
    if "description" in data:
        out["description"] = data["description"]
    return out
