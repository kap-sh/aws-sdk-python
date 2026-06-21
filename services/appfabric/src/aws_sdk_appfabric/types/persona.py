"""Generated from Smithy shape ``com.amazonaws.appfabric#Persona``."""

from typing import Literal, TypeAlias, cast

Persona: TypeAlias = Literal[
    "admin",
    "endUser",
]


# --- restJson1 ser/de ---
def serialize_json(value: Persona) -> str:
    return value


def deserialize_json(data: str) -> Persona:
    return cast(Persona, data)
