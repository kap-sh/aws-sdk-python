"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CreationMode``."""

from typing import Literal, TypeAlias, cast

CreationMode: TypeAlias = Literal[
    "DEFAULT",
    "OVERRIDDEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: CreationMode) -> str:
    return value


def deserialize_json(data: str) -> CreationMode:
    return cast(CreationMode, data)
