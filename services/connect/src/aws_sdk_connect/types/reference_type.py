"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ReferenceType: TypeAlias = Literal[
    "URL",
    "ATTACHMENT",
    "CONTACT_ANALYSIS",
    "NUMBER",
    "STRING",
    "DATE",
    "EMAIL",
    "EMAIL_MESSAGE",
    "EMAIL_MESSAGE_PLAIN_TEXT",
    "EMAIL_MESSAGE_PLAIN_TEXT_REDACTED",
    "EMAIL_MESSAGE_REDACTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "URL",
        "ATTACHMENT",
        "CONTACT_ANALYSIS",
        "NUMBER",
        "STRING",
        "DATE",
        "EMAIL",
        "EMAIL_MESSAGE",
        "EMAIL_MESSAGE_PLAIN_TEXT",
        "EMAIL_MESSAGE_PLAIN_TEXT_REDACTED",
        "EMAIL_MESSAGE_REDACTED",
    )
)


def serialize_json(value: ReferenceType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReferenceType value: {data!r}")
    return cast(ReferenceType, data)
