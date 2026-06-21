"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionReason: TypeAlias = Literal[
    "ACCESS_DENIED",
    "INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)
