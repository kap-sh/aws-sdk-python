"""Generated from Smithy shape ``com.amazonaws.kendra#Persona``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

Persona: TypeAlias = Literal[
    "OWNER",
    "VIEWER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OWNER",
        "VIEWER",
    )
)


def serialize_aws_json_1_1(value: Persona) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Persona:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Persona value: {data!r}")
    return cast(Persona, data)
