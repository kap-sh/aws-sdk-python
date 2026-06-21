"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueHistoryErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetAssetPropertyValueHistoryErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "AccessDeniedException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueHistoryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetAssetPropertyValueHistoryErrorCode:
    return cast(BatchGetAssetPropertyValueHistoryErrorCode, data)
