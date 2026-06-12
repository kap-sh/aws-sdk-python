"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

AnalysisStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_json(value: AnalysisStatus) -> str:
    return value


def deserialize_json(data: str) -> AnalysisStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisStatus value: {data!r}")
    return cast(AnalysisStatus, data)
