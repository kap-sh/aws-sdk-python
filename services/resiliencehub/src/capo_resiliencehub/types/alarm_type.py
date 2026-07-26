"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AlarmType``."""

from typing import Literal, TypeAlias, cast

AlarmType: TypeAlias = Literal[
    "Metric",
    "Composite",
    "Canary",
    "Logs",
    "Event",
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmType) -> str:
    return value


def deserialize_json(data: str) -> AlarmType:
    return cast(AlarmType, data)
