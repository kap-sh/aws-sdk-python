"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2UnprocessedFindingErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

BatchUpdateFindingsV2UnprocessedFindingErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "ValidationException",
    "InternalServerException",
    "ConflictException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceNotFoundException",
        "ValidationException",
        "InternalServerException",
        "ConflictException",
    )
)


def serialize_json(value: BatchUpdateFindingsV2UnprocessedFindingErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchUpdateFindingsV2UnprocessedFindingErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchUpdateFindingsV2UnprocessedFindingErrorCode value: {data!r}"
        )
    return cast(BatchUpdateFindingsV2UnprocessedFindingErrorCode, data)
