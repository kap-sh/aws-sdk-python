"""Generated from Smithy shape ``com.amazonaws.s3files#ImportTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3files.errors import DeserializationError

ImportTrigger: TypeAlias = Literal[
    "ON_DIRECTORY_FIRST_ACCESS",
    "ON_FILE_ACCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DIRECTORY_FIRST_ACCESS",
        "ON_FILE_ACCESS",
    )
)


def serialize_json(value: ImportTrigger) -> str:
    return value


def deserialize_json(data: str) -> ImportTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportTrigger value: {data!r}")
    return cast(ImportTrigger, data)
