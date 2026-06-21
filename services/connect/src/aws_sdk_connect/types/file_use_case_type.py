"""Generated from Smithy shape ``com.amazonaws.connect#FileUseCaseType``."""

from typing import Literal, TypeAlias, cast

FileUseCaseType: TypeAlias = Literal[
    "CONTACT_ANALYSIS",
    "EMAIL_MESSAGE",
    "EMAIL_MESSAGE_PLAIN_TEXT",
    "EMAIL_MESSAGE_REDACTED",
    "EMAIL_MESSAGE_PLAIN_TEXT_REDACTED",
    "ATTACHMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileUseCaseType) -> str:
    return value


def deserialize_json(data: str) -> FileUseCaseType:
    return cast(FileUseCaseType, data)
