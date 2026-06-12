"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchGetAssetPropertyValueErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

BatchGetAssetPropertyValueErrorCode: TypeAlias = Literal[
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


def serialize_json(value: BatchGetAssetPropertyValueErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchGetAssetPropertyValueErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchGetAssetPropertyValueErrorCode value: {data!r}"
        )
    return cast(BatchGetAssetPropertyValueErrorCode, data)
