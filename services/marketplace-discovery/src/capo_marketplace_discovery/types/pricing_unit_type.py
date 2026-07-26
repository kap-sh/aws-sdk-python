"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PricingUnitType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: PricingUnitType) -> str:
    return value


def deserialize_json(data: str) -> PricingUnitType:
    return cast(PricingUnitType, data)
