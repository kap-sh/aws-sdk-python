"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchGetAssetPropertyAggregatesErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "AccessDeniedException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAssetPropertyAggregatesErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetAssetPropertyAggregatesErrorCode:
    return cast(BatchGetAssetPropertyAggregatesErrorCode, data)
