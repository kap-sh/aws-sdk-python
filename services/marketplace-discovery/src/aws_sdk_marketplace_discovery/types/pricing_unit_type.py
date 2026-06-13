"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingUnitType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

PricingUnitType: TypeAlias = Literal[
    "USERS",
    "HOSTS",
    "BANDWIDTH",
    "DATA",
    "TIERS",
    "REQUESTS",
    "UNITS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USERS",
        "HOSTS",
        "BANDWIDTH",
        "DATA",
        "TIERS",
        "REQUESTS",
        "UNITS",
    )
)


def serialize_json(value: PricingUnitType) -> str:
    return value


def deserialize_json(data: str) -> PricingUnitType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingUnitType value: {data!r}")
    return cast(PricingUnitType, data)
