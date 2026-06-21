"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileSourceType``."""

from typing import Literal, TypeAlias, cast

FileSourceType: TypeAlias = Literal[
    "S3",
    "BYTE_CONTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSourceType) -> str:
    return value


def deserialize_json(data: str) -> FileSourceType:
    return cast(FileSourceType, data)
