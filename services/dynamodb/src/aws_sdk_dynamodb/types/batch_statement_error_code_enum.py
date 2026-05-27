"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchStatementErrorCodeEnum``."""

from typing import Literal, TypeAlias

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
