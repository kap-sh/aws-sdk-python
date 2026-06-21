"""Generated from Smithy shape ``com.amazonaws.socialmessaging#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

RegistrationStatus: TypeAlias = Literal[
    "COMPLETE",
    "INCOMPLETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistrationStatus:
    return cast(RegistrationStatus, data)
