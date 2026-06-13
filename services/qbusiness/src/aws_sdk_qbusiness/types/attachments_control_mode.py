"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

AttachmentsControlMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AttachmentsControlMode) -> str:
    return value


def deserialize_json(data: str) -> AttachmentsControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentsControlMode value: {data!r}")
    return cast(AttachmentsControlMode, data)
