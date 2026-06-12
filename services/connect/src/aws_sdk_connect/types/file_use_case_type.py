"""Generated from Smithy shape ``com.amazonaws.connect#FileUseCaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

FileUseCaseType: TypeAlias = Literal[
    "CONTACT_ANALYSIS",
    "EMAIL_MESSAGE",
    "EMAIL_MESSAGE_PLAIN_TEXT",
    "EMAIL_MESSAGE_REDACTED",
    "EMAIL_MESSAGE_PLAIN_TEXT_REDACTED",
    "ATTACHMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTACT_ANALYSIS",
        "EMAIL_MESSAGE",
        "EMAIL_MESSAGE_PLAIN_TEXT",
        "EMAIL_MESSAGE_REDACTED",
        "EMAIL_MESSAGE_PLAIN_TEXT_REDACTED",
        "ATTACHMENT",
    )
)


def serialize_json(value: FileUseCaseType) -> str:
    return value


def deserialize_json(data: str) -> FileUseCaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileUseCaseType value: {data!r}")
    return cast(FileUseCaseType, data)
