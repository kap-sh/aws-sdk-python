"""Generated from Smithy shape ``com.amazonaws.repostspace#FeatureEnableParameter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

FeatureEnableParameter: TypeAlias = Literal[
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


def serialize_json(value: FeatureEnableParameter) -> str:
    return value


def deserialize_json(data: str) -> FeatureEnableParameter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureEnableParameter value: {data!r}")
    return cast(FeatureEnableParameter, data)
