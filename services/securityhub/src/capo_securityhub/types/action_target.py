"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ActionTarget(TypedDict, closed=True):
    action_target_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN for the target action.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the action target.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The description of the target action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionTarget) -> dict:
    out: dict = {}
    if "action_target_arn" in value:
        out["ActionTargetArn"] = value["action_target_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ActionTarget:
    out: ActionTarget = {}  # type: ignore[typeddict-item]
    if "ActionTargetArn" in data:
        out["action_target_arn"] = data["ActionTargetArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
