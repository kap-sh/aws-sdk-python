"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitStatus``."""

from typing import Literal, TypeAlias, cast

BenefitStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BenefitStatus:
    return cast(BenefitStatus, data)
