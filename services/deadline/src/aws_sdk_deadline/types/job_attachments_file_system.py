"""Generated from Smithy shape ``com.amazonaws.deadline#JobAttachmentsFileSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

JobAttachmentsFileSystem: TypeAlias = Literal[
    "COPIED",
    "VIRTUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COPIED",
        "VIRTUAL",
    )
)


def serialize_json(value: JobAttachmentsFileSystem) -> str:
    return value


def deserialize_json(data: str) -> JobAttachmentsFileSystem:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobAttachmentsFileSystem value: {data!r}")
    return cast(JobAttachmentsFileSystem, data)
