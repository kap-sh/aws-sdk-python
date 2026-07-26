"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntityErrorCode``."""

from typing import Literal, TypeAlias, cast

JobEntityErrorCode: TypeAlias = Literal[
    "AccessDeniedException",
    "InternalServerException",
    "ValidationException",
    "ResourceNotFoundException",
    "MaxPayloadSizeExceeded",
    "ConflictException",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobEntityErrorCode) -> str:
    return value


def deserialize_json(data: str) -> JobEntityErrorCode:
    return cast(JobEntityErrorCode, data)
