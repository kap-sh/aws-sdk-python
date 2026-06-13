"""Generated from Smithy shape ``com.amazonaws.bedrock#S3InputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

S3InputFormat: TypeAlias = Literal["JSONL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JSONL",))


def serialize_json(value: S3InputFormat) -> str:
    return value


def deserialize_json(data: str) -> S3InputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3InputFormat value: {data!r}")
    return cast(S3InputFormat, data)
