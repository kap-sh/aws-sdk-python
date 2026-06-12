"""Generated from Smithy shape ``com.amazonaws.guardduty#FeatureStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

FeatureStatus: TypeAlias = Literal[
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


def serialize_json(value: FeatureStatus) -> str:
    return value


def deserialize_json(data: str) -> FeatureStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureStatus value: {data!r}")
    return cast(FeatureStatus, data)
