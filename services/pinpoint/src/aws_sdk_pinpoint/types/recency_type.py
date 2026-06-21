"""Generated from Smithy shape ``com.amazonaws.pinpoint#RecencyType``."""

from typing import Literal, TypeAlias, cast

RecencyType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecencyType) -> str:
    return value


def deserialize_json(data: str) -> RecencyType:
    return cast(RecencyType, data)
