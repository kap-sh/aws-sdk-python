"""Generated from Smithy shape ``com.amazonaws.connect#MonitorCapability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

MonitorCapability: TypeAlias = Literal[
    "SILENT_MONITOR",
    "BARGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SILENT_MONITOR",
        "BARGE",
    )
)


def serialize_json(value: MonitorCapability) -> str:
    return value


def deserialize_json(data: str) -> MonitorCapability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorCapability value: {data!r}")
    return cast(MonitorCapability, data)
