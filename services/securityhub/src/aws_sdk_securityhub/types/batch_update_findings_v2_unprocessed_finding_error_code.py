"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateFindingsV2UnprocessedFindingErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchUpdateFindingsV2UnprocessedFindingErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "ValidationException",
    "InternalServerException",
    "ConflictException",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateFindingsV2UnprocessedFindingErrorCode) -> str:
    return value


def deserialize_json(data: str) -> BatchUpdateFindingsV2UnprocessedFindingErrorCode:
    return cast(BatchUpdateFindingsV2UnprocessedFindingErrorCode, data)
