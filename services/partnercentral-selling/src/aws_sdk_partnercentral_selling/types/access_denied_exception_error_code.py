"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AccessDeniedExceptionErrorCode``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionErrorCode: TypeAlias = Literal[
    "INCOMPATIBLE_BENEFIT_AWS_PARTNER_STATE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedExceptionErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessDeniedExceptionErrorCode:
    return cast(AccessDeniedExceptionErrorCode, data)
