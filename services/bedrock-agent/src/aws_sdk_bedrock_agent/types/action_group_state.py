"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupState``."""

from typing import Literal, TypeAlias, cast

ActionGroupState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupState) -> str:
    return value


def deserialize_json(data: str) -> ActionGroupState:
    return cast(ActionGroupState, data)
