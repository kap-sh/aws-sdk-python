"""Generated from Smithy shape ``com.amazonaws.artifact#UploadState``."""

from typing import Literal, TypeAlias, cast

UploadState: TypeAlias = Literal[
    "PROCESSING",
    "COMPLETE",
    "FAILED",
    "FAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: UploadState) -> str:
    return value


def deserialize_json(data: str) -> UploadState:
    return cast(UploadState, data)
