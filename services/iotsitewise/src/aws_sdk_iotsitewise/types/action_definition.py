"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name


class ActionDefinition(TypedDict, closed=True):
    action_definition_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the action definition.</p>"""
    action_name: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The name of the action definition.</p>"""
    action_type: "aws_sdk_iotsitewise.types.name.Name"
    """<p>The type of the action definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionDefinition) -> dict:
    out: dict = {}
    out["actionDefinitionId"] = value["action_definition_id"]
    out["actionName"] = value["action_name"]
    out["actionType"] = value["action_type"]
    return out


def deserialize_json(data: dict) -> ActionDefinition:
    out: ActionDefinition = {}  # type: ignore[typeddict-item]
    if "actionDefinitionId" in data:
        out["action_definition_id"] = data["actionDefinitionId"]
    else:
        raise DeserializationError("ActionDefinition.action_definition_id required")
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    else:
        raise DeserializationError("ActionDefinition.action_name required")
    if "actionType" in data:
        out["action_type"] = data["actionType"]
    else:
        raise DeserializationError("ActionDefinition.action_type required")
    return out
