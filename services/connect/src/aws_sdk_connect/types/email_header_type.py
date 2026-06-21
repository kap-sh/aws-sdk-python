"""Generated from Smithy shape ``com.amazonaws.connect#EmailHeaderType``."""

from typing import Literal, TypeAlias, cast

EmailHeaderType: TypeAlias = Literal[
    "REFERENCES",
    "MESSAGE_ID",
    "IN_REPLY_TO",
    "X_SES_SPAM_VERDICT",
    "X_SES_VIRUS_VERDICT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailHeaderType) -> str:
    return value


def deserialize_json(data: str) -> EmailHeaderType:
    return cast(EmailHeaderType, data)
