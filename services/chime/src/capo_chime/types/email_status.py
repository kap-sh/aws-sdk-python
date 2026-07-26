"""Generated from Smithy shape ``com.amazonaws.chime#EmailStatus``."""

from typing import Literal, TypeAlias, cast

EmailStatus: TypeAlias = Literal[
    "NotSent",
    "Sent",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailStatus) -> str:
    return value


def deserialize_json(data: str) -> EmailStatus:
    return cast(EmailStatus, data)
