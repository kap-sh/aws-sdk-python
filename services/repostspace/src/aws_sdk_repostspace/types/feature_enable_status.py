"""Generated from Smithy shape ``com.amazonaws.repostspace#FeatureEnableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

FeatureEnableStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "NOT_ALLOWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "NOT_ALLOWED",
    )
)


def serialize_json(value: FeatureEnableStatus) -> str:
    return value


def deserialize_json(data: str) -> FeatureEnableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureEnableStatus value: {data!r}")
    return cast(FeatureEnableStatus, data)
