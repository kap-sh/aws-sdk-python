"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DimensionLabelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

DimensionLabelType: TypeAlias = Literal[
    "Region",
    "SagemakerOption",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Region",
        "SagemakerOption",
    )
)


def serialize_json(value: DimensionLabelType) -> str:
    return value


def deserialize_json(data: str) -> DimensionLabelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionLabelType value: {data!r}")
    return cast(DimensionLabelType, data)
