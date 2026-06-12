"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

DetectionSource: TypeAlias = Literal[
    "AMAZON",
    "BITDEFENDER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMAZON",
        "BITDEFENDER",
    )
)


def serialize_json(value: DetectionSource) -> str:
    return value


def deserialize_json(data: str) -> DetectionSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetectionSource value: {data!r}")
    return cast(DetectionSource, data)
