"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ReferenceType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceType:
    return cast(ReferenceType, data)
