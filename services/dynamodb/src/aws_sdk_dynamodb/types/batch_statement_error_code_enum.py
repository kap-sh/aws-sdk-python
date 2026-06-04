"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementErrorCodeEnum``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

BatchStatementErrorCodeEnum: TypeAlias = Literal[
    "ConditionalCheckFailed",
    "ItemCollectionSizeLimitExceeded",
    "RequestLimitExceeded",
    "ValidationError",
    "ProvisionedThroughputExceeded",
    "TransactionConflict",
    "ThrottlingError",
    "InternalServerError",
    "ResourceNotFound",
    "AccessDenied",
    "DuplicateItem",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConditionalCheckFailed",
        "ItemCollectionSizeLimitExceeded",
        "RequestLimitExceeded",
        "ValidationError",
        "ProvisionedThroughputExceeded",
        "TransactionConflict",
        "ThrottlingError",
        "InternalServerError",
        "ResourceNotFound",
        "AccessDenied",
        "DuplicateItem",
    )
)


def serialize_aws_json_1_0(value: BatchStatementErrorCodeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchStatementErrorCodeEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchStatementErrorCodeEnum value: {data!r}"
        )
    return cast(BatchStatementErrorCodeEnum, data)
