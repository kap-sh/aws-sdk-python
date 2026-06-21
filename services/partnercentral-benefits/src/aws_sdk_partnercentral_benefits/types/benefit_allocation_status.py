"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitAllocationStatus``."""

from typing import Literal, TypeAlias, cast

BenefitAllocationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "FULFILLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitAllocationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BenefitAllocationStatus:
    return cast(BenefitAllocationStatus, data)
