"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ActionIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.action_id
    import aws_sdk_verifiedpermissions.types.action_type


class ActionIdentifier(TypedDict, closed=True):
    action_type: "aws_sdk_verifiedpermissions.types.action_type.ActionType"
    """<p>The type of an action.</p>"""
    action_id: "aws_sdk_verifiedpermissions.types.action_id.ActionId"
    """<p>The ID of an action.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionIdentifier) -> dict:
    out: dict = {}
    out["actionType"] = value["action_type"]
    out["actionId"] = value["action_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActionIdentifier:
    out: ActionIdentifier = {}  # type: ignore[typeddict-item]
    if "actionType" in data:
        out["action_type"] = data["actionType"]
    else:
        raise DeserializationError("ActionIdentifier.action_type required")
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("ActionIdentifier.action_id required")
    return out
