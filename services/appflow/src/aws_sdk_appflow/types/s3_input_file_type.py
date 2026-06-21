"""Generated from Smithy shape ``com.amazonaws.appflow#S3InputFileType``."""

from typing import Literal, TypeAlias, cast

S3InputFileType: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3InputFileType) -> str:
    return value


def deserialize_json(data: str) -> S3InputFileType:
    return cast(S3InputFileType, data)
