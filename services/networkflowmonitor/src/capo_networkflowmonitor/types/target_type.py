"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TargetType``."""

from typing import Literal, TypeAlias, cast

TargetType: TypeAlias = Literal["ACCOUNT",]


# --- restJson1 ser/de ---
def serialize_json(value: TargetType) -> str:
    return value


def deserialize_json(data: str) -> TargetType:
    return cast(TargetType, data)
