"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

DeliveryStreamFailureType: TypeAlias = Literal[
    "VPC_ENDPOINT_SERVICE_NAME_NOT_FOUND",
    "VPC_INTERFACE_ENDPOINT_SERVICE_ACCESS_DENIED",
    "RETIRE_KMS_GRANT_FAILED",
    "CREATE_KMS_GRANT_FAILED",
    "KMS_ACCESS_DENIED",
    "DISABLED_KMS_KEY",
    "INVALID_KMS_KEY",
    "KMS_KEY_NOT_FOUND",
    "KMS_OPT_IN_REQUIRED",
    "CREATE_ENI_FAILED",
    "DELETE_ENI_FAILED",
    "SUBNET_NOT_FOUND",
    "SECURITY_GROUP_NOT_FOUND",
    "ENI_ACCESS_DENIED",
    "SUBNET_ACCESS_DENIED",
    "SECURITY_GROUP_ACCESS_DENIED",
    "UNKNOWN_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VPC_ENDPOINT_SERVICE_NAME_NOT_FOUND",
        "VPC_INTERFACE_ENDPOINT_SERVICE_ACCESS_DENIED",
        "RETIRE_KMS_GRANT_FAILED",
        "CREATE_KMS_GRANT_FAILED",
        "KMS_ACCESS_DENIED",
        "DISABLED_KMS_KEY",
        "INVALID_KMS_KEY",
        "KMS_KEY_NOT_FOUND",
        "KMS_OPT_IN_REQUIRED",
        "CREATE_ENI_FAILED",
        "DELETE_ENI_FAILED",
        "SUBNET_NOT_FOUND",
        "SECURITY_GROUP_NOT_FOUND",
        "ENI_ACCESS_DENIED",
        "SUBNET_ACCESS_DENIED",
        "SECURITY_GROUP_ACCESS_DENIED",
        "UNKNOWN_ERROR",
    )
)


def serialize_aws_json_1_1(value: DeliveryStreamFailureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryStreamFailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryStreamFailureType value: {data!r}")
    return cast(DeliveryStreamFailureType, data)
