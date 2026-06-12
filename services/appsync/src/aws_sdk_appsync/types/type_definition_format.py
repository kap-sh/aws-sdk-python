"""Generated from Smithy shape ``com.amazonaws.appsync#TypeDefinitionFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

TypeDefinitionFormat: TypeAlias = Literal[
    "SDL",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SDL",
        "JSON",
    )
)


def serialize_json(value: TypeDefinitionFormat) -> str:
    return value


def deserialize_json(data: str) -> TypeDefinitionFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TypeDefinitionFormat value: {data!r}")
    return cast(TypeDefinitionFormat, data)
