"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetAssetPropertyValueErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "AccessDeniedException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyValueErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetAssetPropertyValueErrorCode:
    return cast(BatchGetAssetPropertyValueErrorCode, data)
