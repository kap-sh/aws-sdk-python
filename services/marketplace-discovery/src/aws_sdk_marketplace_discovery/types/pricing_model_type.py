"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

PricingModelType: TypeAlias = Literal[
    "USAGE",
    "CONTRACT",
    "BYOL",
    "FREE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USAGE",
        "CONTRACT",
        "BYOL",
        "FREE",
    )
)


def serialize_json(value: PricingModelType) -> str:
    return value


def deserialize_json(data: str) -> PricingModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingModelType value: {data!r}")
    return cast(PricingModelType, data)
