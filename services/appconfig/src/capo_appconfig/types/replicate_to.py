"""Generated from Smithy shape ``com.amazonaws.appconfig#ReplicateTo``."""

from typing import Literal, TypeAlias, cast

ReplicateTo: TypeAlias = Literal[
    "NONE",
    "SSM_DOCUMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicateTo) -> str:
    return value


def deserialize_json(data: str) -> ReplicateTo:
    return cast(ReplicateTo, data)
