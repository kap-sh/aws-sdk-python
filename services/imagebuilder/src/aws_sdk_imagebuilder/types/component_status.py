"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentStatus``."""

from typing import Literal, TypeAlias, cast

ComponentStatus: TypeAlias = Literal[
    "DEPRECATED",
    "DISABLED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentStatus) -> str:
    return value


def deserialize_json(data: str) -> ComponentStatus:
    return cast(ComponentStatus, data)
