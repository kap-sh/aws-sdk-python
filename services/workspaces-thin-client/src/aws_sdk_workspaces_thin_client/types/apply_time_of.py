"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ApplyTimeOf``."""

from typing import Literal, TypeAlias, cast

ApplyTimeOf: TypeAlias = Literal[
    "UTC",
    "DEVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplyTimeOf) -> str:
    return value


def deserialize_json(data: str) -> ApplyTimeOf:
    return cast(ApplyTimeOf, data)
