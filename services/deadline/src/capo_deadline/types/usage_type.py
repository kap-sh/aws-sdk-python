"""Generated from Smithy shape ``com.amazonaws.deadline#UsageType``."""

from typing import Literal, TypeAlias, cast

UsageType: TypeAlias = Literal[
    "COMPUTE",
    "LICENSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageType) -> str:
    return value


def deserialize_json(data: str) -> UsageType:
    return cast(UsageType, data)
