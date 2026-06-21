"""Generated from Smithy shape ``com.amazonaws.sesv2#MailType``."""

from typing import Literal, TypeAlias, cast

MailType: TypeAlias = Literal[
    "MARKETING",
    "TRANSACTIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MailType) -> str:
    return value


def deserialize_json(data: str) -> MailType:
    return cast(MailType, data)
