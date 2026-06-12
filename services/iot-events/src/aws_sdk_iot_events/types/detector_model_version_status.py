"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

DetectorModelVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ACTIVATING",
    "INACTIVE",
    "DEPRECATED",
    "DRAFT",
    "PAUSED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ACTIVATING",
        "INACTIVE",
        "DEPRECATED",
        "DRAFT",
        "PAUSED",
        "FAILED",
    )
)


def serialize_json(value: DetectorModelVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectorModelVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DetectorModelVersionStatus value: {data!r}"
        )
    return cast(DetectorModelVersionStatus, data)
