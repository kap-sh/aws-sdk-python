"""Generated from Smithy shape ``com.amazonaws.eventbridge#Level``."""

from typing import Literal, TypeAlias, cast

Level: TypeAlias = Literal[
    "OFF",
    "ERROR",
    "INFO",
    "TRACE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Level) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Level:
    return cast(Level, data)
