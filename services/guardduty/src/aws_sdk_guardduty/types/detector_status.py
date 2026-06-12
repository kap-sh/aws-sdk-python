"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

DetectorStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DetectorStatus) -> str:
    return value


def deserialize_json(data: str) -> DetectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetectorStatus value: {data!r}")
    return cast(DetectorStatus, data)
