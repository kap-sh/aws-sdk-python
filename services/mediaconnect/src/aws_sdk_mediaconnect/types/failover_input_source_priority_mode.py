"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverInputSourcePriorityMode``."""

from typing import Literal, TypeAlias, cast

FailoverInputSourcePriorityMode: TypeAlias = Literal[
    "NO_PRIORITY",
    "PRIMARY_SECONDARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailoverInputSourcePriorityMode) -> str:
    return value


def deserialize_json(data: str) -> FailoverInputSourcePriorityMode:
    return cast(FailoverInputSourcePriorityMode, data)
