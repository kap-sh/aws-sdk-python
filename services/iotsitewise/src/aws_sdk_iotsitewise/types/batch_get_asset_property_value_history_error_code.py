"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

BatchGetAssetPropertyValueHistoryErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "AccessDeniedException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceNotFoundException",
        "InvalidRequestException",
        "AccessDeniedException",
    )
)


def serialize_json(value: BatchGetAssetPropertyValueHistoryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetAssetPropertyValueHistoryErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchGetAssetPropertyValueHistoryErrorCode value: {data!r}"
        )
    return cast(BatchGetAssetPropertyValueHistoryErrorCode, data)
