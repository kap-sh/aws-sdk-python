"""Generated from Smithy shape ``com.amazonaws.sesv2#MailType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

MailType: TypeAlias = Literal[
    "MARKETING",
    "TRANSACTIONAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MARKETING",
        "TRANSACTIONAL",
    )
)


def serialize_json(value: MailType) -> str:
    return value


def deserialize_json(data: str) -> MailType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MailType value: {data!r}")
    return cast(MailType, data)
