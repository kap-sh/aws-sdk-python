"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ActionDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.action_definition

ActionDefinitions: TypeAlias = list[
    "aws_sdk_iotsitewise.types.action_definition.ActionDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionDefinitions) -> list:
    import aws_sdk_iotsitewise.types.action_definition

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.action_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionDefinitions:
    import aws_sdk_iotsitewise.types.action_definition

    out: ActionDefinitions = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.action_definition.deserialize_json(item))
    return out
