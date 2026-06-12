"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FeatureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

FeatureType: TypeAlias = Literal[
    "TEXTUAL",
    "CATEGORICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXTUAL",
        "CATEGORICAL",
    )
)


def serialize_json(value: FeatureType) -> str:
    return value


def deserialize_json(data: str) -> FeatureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureType value: {data!r}")
    return cast(FeatureType, data)
