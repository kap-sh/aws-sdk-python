"""Generated from Smithy shape ``com.amazonaws.artifact#UploadState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_artifact.errors import DeserializationError

UploadState: TypeAlias = Literal[
    "PROCESSING",
    "COMPLETE",
    "FAILED",
    "FAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "COMPLETE",
        "FAILED",
        "FAULT",
    )
)


def serialize_json(value: UploadState) -> str:
    return value


def deserialize_json(data: str) -> UploadState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UploadState value: {data!r}")
    return cast(UploadState, data)
