"""Generated from Smithy shape ``com.amazonaws.deadline#ResponseBudgetAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.budget_action_type
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.threshold_percentage


class ResponseBudgetAction(TypedDict, closed=True):
    type: "aws_sdk_deadline.types.budget_action_type.BudgetActionType"
    """<p>The action taken on the budget once scheduling stops.</p>"""
    threshold_percentage: (
        "aws_sdk_deadline.types.threshold_percentage.ThresholdPercentage"
    )
    """<p>The percentage threshold for the budget.</p>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The budget action description.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseBudgetAction) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.budget_action_type

    out["type"] = aws_sdk_deadline.types.budget_action_type.serialize_json(
        value["type"]
    )
    out["thresholdPercentage"] = value["threshold_percentage"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ResponseBudgetAction:
    out: ResponseBudgetAction = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_deadline.types.budget_action_type

        out["type"] = aws_sdk_deadline.types.budget_action_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ResponseBudgetAction.type required")
    if "thresholdPercentage" in data:
        out["threshold_percentage"] = data["thresholdPercentage"]
    else:
        raise DeserializationError("ResponseBudgetAction.threshold_percentage required")
    if "description" in data:
        out["description"] = data["description"]
    return out
