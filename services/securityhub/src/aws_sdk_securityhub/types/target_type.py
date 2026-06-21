"""Generated from Smithy shape ``com.amazonaws.securityhub#TargetType``."""

from typing import Literal, TypeAlias, cast

TargetType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATIONAL_UNIT",
    "ROOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetType) -> str:
    return value


def deserialize_json(data: str) -> TargetType:
    return cast(TargetType, data)
