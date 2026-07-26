"""Generated from Smithy shape ``com.amazonaws.iot#AutoRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

AutoRegistrationStatus: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoRegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoRegistrationStatus:
    return cast(AutoRegistrationStatus, data)
