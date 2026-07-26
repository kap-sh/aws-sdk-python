"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyValueErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchPutAssetPropertyValueErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "InternalFailureException",
    "ServiceUnavailableException",
    "ThrottlingException",
    "LimitExceededException",
    "ConflictingOperationException",
    "TimestampOutOfRangeException",
    "AccessDeniedException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAssetPropertyValueErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchPutAssetPropertyValueErrorCode:
    return cast(BatchPutAssetPropertyValueErrorCode, data)
