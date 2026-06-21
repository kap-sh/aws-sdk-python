"""Generated from Smithy shape ``com.amazonaws.pcs#SpotAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

SpotAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "capacity-optimized",
    "price-capacity-optimized",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpotAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpotAllocationStrategy:
    return cast(SpotAllocationStrategy, data)
