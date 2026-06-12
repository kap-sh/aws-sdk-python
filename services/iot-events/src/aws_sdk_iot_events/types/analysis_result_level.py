"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisResultLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

AnalysisResultLevel: TypeAlias = Literal[
    "INFO",
    "WARNING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFO",
        "WARNING",
        "ERROR",
    )
)


def serialize_json(value: AnalysisResultLevel) -> str:
    return value


def deserialize_json(data: str) -> AnalysisResultLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisResultLevel value: {data!r}")
    return cast(AnalysisResultLevel, data)
