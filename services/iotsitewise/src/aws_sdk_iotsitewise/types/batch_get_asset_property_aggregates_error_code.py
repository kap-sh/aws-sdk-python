"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyAggregatesErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

BatchGetAssetPropertyAggregatesErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchGetAssetPropertyAggregatesErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetAssetPropertyAggregatesErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchGetAssetPropertyAggregatesErrorCode value: {data!r}"
        )
    return cast(BatchGetAssetPropertyAggregatesErrorCode, data)
