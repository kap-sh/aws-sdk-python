"""Generated from Smithy shape ``com.amazonaws.appfabric#Persona``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

Persona: TypeAlias = Literal[
    "admin",
    "endUser",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "admin",
        "endUser",
    )
)


def serialize_json(value: Persona) -> str:
    return value


def deserialize_json(data: str) -> Persona:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Persona value: {data!r}")
    return cast(Persona, data)
