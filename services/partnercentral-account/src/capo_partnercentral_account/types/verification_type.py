"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationType``."""

from typing import Literal, TypeAlias, cast

VerificationType: TypeAlias = Literal[
    "BUSINESS_VERIFICATION",
    "REGISTRANT_VERIFICATION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VerificationType:
    return cast(VerificationType, data)
