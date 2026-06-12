"""Generated from Smithy shape ``com.amazonaws.appflow#S3InputFileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

S3InputFileType: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSON",
    )
)


def serialize_json(value: S3InputFileType) -> str:
    return value


def deserialize_json(data: str) -> S3InputFileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3InputFileType value: {data!r}")
    return cast(S3InputFileType, data)
