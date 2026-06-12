"""Generated from Smithy shape ``com.amazonaws.lightsail#PricingUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

PricingUnit: TypeAlias = Literal[
    "GB",
    "Hrs",
    "GB-Mo",
    "Bundles",
    "Queries",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GB",
        "Hrs",
        "GB-Mo",
        "Bundles",
        "Queries",
    )
)


def serialize_aws_json_1_1(value: PricingUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PricingUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PricingUnit value: {data!r}")
    return cast(PricingUnit, data)
