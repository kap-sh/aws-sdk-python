"""Generated from Smithy shape ``com.amazonaws.connect#MeetingFeatureStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

MeetingFeatureStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UNAVAILABLE",
    )
)


def serialize_json(value: MeetingFeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> MeetingFeatureStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MeetingFeatureStatus value: {data!r}")
    return cast(MeetingFeatureStatus, data)
