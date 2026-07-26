"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

VerificationStatus: TypeAlias = Literal[
    "PENDING_CUSTOMER_ACTION",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
    "REJECTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VerificationStatus:
    return cast(VerificationStatus, data)
