"""Generated from Smithy shape ``com.amazonaws.acm#FailureReason``."""

from typing import Literal, TypeAlias, cast

FailureReason: TypeAlias = Literal[
    "NO_AVAILABLE_CONTACTS",
    "ADDITIONAL_VERIFICATION_REQUIRED",
    "DOMAIN_NOT_ALLOWED",
    "INVALID_PUBLIC_DOMAIN",
    "DOMAIN_VALIDATION_DENIED",
    "CAA_ERROR",
    "PCA_LIMIT_EXCEEDED",
    "PCA_INVALID_ARN",
    "PCA_INVALID_STATE",
    "PCA_REQUEST_FAILED",
    "PCA_NAME_CONSTRAINTS_VALIDATION",
    "PCA_RESOURCE_NOT_FOUND",
    "PCA_INVALID_ARGS",
    "PCA_INVALID_DURATION",
    "PCA_ACCESS_DENIED",
    "SLR_NOT_FOUND",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureReason:
    return cast(FailureReason, data)
