"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareFeatureSet``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

ResourceShareFeatureSet: TypeAlias = Literal[
    "CREATED_FROM_POLICY",
    "PROMOTING_TO_STANDARD",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED_FROM_POLICY",
        "PROMOTING_TO_STANDARD",
        "STANDARD",
    )
)


def serialize_json(value: ResourceShareFeatureSet) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareFeatureSet:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceShareFeatureSet value: {data!r}")
    return cast(ResourceShareFeatureSet, data)
