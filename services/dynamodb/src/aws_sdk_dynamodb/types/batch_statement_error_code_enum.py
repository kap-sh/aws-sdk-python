"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementErrorCodeEnum``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: BatchStatementErrorCodeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchStatementErrorCodeEnum:
    return cast(BatchStatementErrorCodeEnum, data)
