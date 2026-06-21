"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Trace``."""

from typing import Literal, TypeAlias, cast

Trace: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLED_FULL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> str:
    return value


def deserialize_json(data: str) -> Trace:
    return cast(Trace, data)
