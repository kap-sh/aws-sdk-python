"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandProvisioningAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

OnDemandProvisioningAllocationStrategy: TypeAlias = Literal[
    "lowest-price",
    "prioritized",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDemandProvisioningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandProvisioningAllocationStrategy:
    return cast(OnDemandProvisioningAllocationStrategy, data)
