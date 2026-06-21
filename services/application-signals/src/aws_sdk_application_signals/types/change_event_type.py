"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ChangeEventType``."""

from typing import Literal, TypeAlias, cast

ChangeEventType: TypeAlias = Literal[
    "DEPLOYMENT",
    "CONFIGURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeEventType) -> str:
    return value


def deserialize_json(data: str) -> ChangeEventType:
    return cast(ChangeEventType, data)
