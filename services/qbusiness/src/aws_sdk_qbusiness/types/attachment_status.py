"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

AttachmentStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCESS",
    )
)


def serialize_json(value: AttachmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AttachmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentStatus value: {data!r}")
    return cast(AttachmentStatus, data)
