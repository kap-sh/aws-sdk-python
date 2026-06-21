"""Generated from Smithy shape ``com.amazonaws.lightsail#PricingUnit``."""

from typing import Literal, TypeAlias, cast

PricingUnit: TypeAlias = Literal[
    "GB",
    "Hrs",
    "GB-Mo",
    "Bundles",
    "Queries",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PricingUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PricingUnit:
    return cast(PricingUnit, data)
