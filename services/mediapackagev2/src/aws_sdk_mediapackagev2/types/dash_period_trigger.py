"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashPeriodTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashPeriodTrigger: TypeAlias = Literal[
    "AVAILS",
    "DRM_KEY_ROTATION",
    "SOURCE_CHANGES",
    "SOURCE_DISRUPTIONS",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILS",
        "DRM_KEY_ROTATION",
        "SOURCE_CHANGES",
        "SOURCE_DISRUPTIONS",
        "NONE",
    )
)


def serialize_json(value: DashPeriodTrigger) -> str:
    return value


def deserialize_json(data: str) -> DashPeriodTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashPeriodTrigger value: {data!r}")
    return cast(DashPeriodTrigger, data)
