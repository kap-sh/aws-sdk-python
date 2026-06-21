"""Generated from Smithy shape ``com.amazonaws.emr#SpotProvisioningAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

SpotProvisioningAllocationStrategy: TypeAlias = Literal[
    "capacity-optimized",
    "price-capacity-optimized",
    "lowest-price",
    "diversified",
    "capacity-optimized-prioritized",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpotProvisioningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpotProvisioningAllocationStrategy:
    return cast(SpotProvisioningAllocationStrategy, data)
