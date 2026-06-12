"""Generated from Smithy shape ``com.amazonaws.connect#EmailHeaderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EmailHeaderType: TypeAlias = Literal[
    "REFERENCES",
    "MESSAGE_ID",
    "IN_REPLY_TO",
    "X_SES_SPAM_VERDICT",
    "X_SES_VIRUS_VERDICT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REFERENCES",
        "MESSAGE_ID",
        "IN_REPLY_TO",
        "X_SES_SPAM_VERDICT",
        "X_SES_VIRUS_VERDICT",
    )
)


def serialize_json(value: EmailHeaderType) -> str:
    return value


def deserialize_json(data: str) -> EmailHeaderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmailHeaderType value: {data!r}")
    return cast(EmailHeaderType, data)
