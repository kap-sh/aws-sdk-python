"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchPutAssetPropertyValueErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceNotFoundException",
        "InvalidRequestException",
        "InternalFailureException",
        "ServiceUnavailableException",
        "ThrottlingException",
        "LimitExceededException",
        "ConflictingOperationException",
        "TimestampOutOfRangeException",
        "AccessDeniedException",
    )
)


def serialize_json(value: BatchPutAssetPropertyValueErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchPutAssetPropertyValueErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchPutAssetPropertyValueErrorCode value: {data!r}"
        )
    return cast(BatchPutAssetPropertyValueErrorCode, data)
