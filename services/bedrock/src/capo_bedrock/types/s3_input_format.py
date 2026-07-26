"""Generated from Smithy shape ``com.amazonaws.bedrock#S3InputFormat``."""

from typing import Literal, TypeAlias, cast

S3InputFormat: TypeAlias = Literal["JSONL",]


# --- restJson1 ser/de ---
def serialize_json(value: S3InputFormat) -> str:
    return value


def deserialize_json(data: str) -> S3InputFormat:
    return cast(S3InputFormat, data)
