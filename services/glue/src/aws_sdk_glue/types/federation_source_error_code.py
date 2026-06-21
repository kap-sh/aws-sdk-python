"""Generated from Smithy shape ``com.amazonaws.glue#FederationSourceErrorCode``."""

from typing import Literal, TypeAlias, cast

FederationSourceErrorCode: TypeAlias = Literal[
    "AccessDeniedException",
    "EntityNotFoundException",
    "InvalidCredentialsException",
    "InvalidInputException",
    "InvalidResponseException",
    "OperationTimeoutException",
    "OperationNotSupportedException",
    "InternalServiceException",
    "PartialFailureException",
    "ThrottlingException",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationSourceErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FederationSourceErrorCode:
    return cast(FederationSourceErrorCode, data)
