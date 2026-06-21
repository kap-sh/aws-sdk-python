"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitApplicationStatus``."""

from typing import Literal, TypeAlias, cast

BenefitApplicationStatus: TypeAlias = Literal[
    "PENDING_SUBMISSION",
    "IN_REVIEW",
    "ACTION_REQUIRED",
    "APPROVED",
    "REJECTED",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BenefitApplicationStatus:
    return cast(BenefitApplicationStatus, data)
