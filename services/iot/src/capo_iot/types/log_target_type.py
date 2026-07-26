"""Generated from Smithy shape ``com.amazonaws.iot#LogTargetType``."""

from typing import Literal, TypeAlias, cast

LogTargetType: TypeAlias = Literal[
    "DEFAULT",
    "THING_GROUP",
    "CLIENT_ID",
    "SOURCE_IP",
    "PRINCIPAL_ID",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogTargetType) -> str:
    return value


def deserialize_json(data: str) -> LogTargetType:
    return cast(LogTargetType, data)
