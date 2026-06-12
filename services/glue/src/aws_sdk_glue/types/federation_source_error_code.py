"""Generated from Smithy shape ``com.amazonaws.glue#FederationSourceErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: FederationSourceErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FederationSourceErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FederationSourceErrorCode value: {data!r}")
    return cast(FederationSourceErrorCode, data)
