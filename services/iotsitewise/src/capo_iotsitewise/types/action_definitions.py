"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ActionDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_definition

ActionDefinitions: TypeAlias = list[
    "capo_iotsitewise.types.action_definition.ActionDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionDefinitions) -> list:
    import capo_iotsitewise.types.action_definition

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.action_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionDefinitions:
    import capo_iotsitewise.types.action_definition

    out: ActionDefinitions = []
    for item in data:
        out.append(capo_iotsitewise.types.action_definition.deserialize_json(item))
    return out
