"""Generated from Smithy shape ``com.amazonaws.appconfig#TriggeredBy``."""

from typing import Literal, TypeAlias, cast

TriggeredBy: TypeAlias = Literal[
    "USER",
    "APPCONFIG",
    "CLOUDWATCH_ALARM",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggeredBy) -> str:
    return value


def deserialize_json(data: str) -> TriggeredBy:
    return cast(TriggeredBy, data)
