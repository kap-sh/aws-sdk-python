"""Generated from Smithy shape ``com.amazonaws.wafv2#FailureReason``."""

from typing import Literal, TypeAlias, cast

FailureReason: TypeAlias = Literal[
    "TOKEN_MISSING",
    "TOKEN_EXPIRED",
    "TOKEN_INVALID",
    "TOKEN_DOMAIN_MISMATCH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureReason:
    return cast(FailureReason, data)
