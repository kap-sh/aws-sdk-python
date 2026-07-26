"""Generated from Smithy shape ``com.amazonaws.chime#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

RegistrationStatus: TypeAlias = Literal[
    "Unregistered",
    "Registered",
    "Suspended",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistrationStatus:
    return cast(RegistrationStatus, data)
