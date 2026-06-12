"""Generated from Smithy shape ``com.amazonaws.schemas#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_schemas.errors import DeserializationError

Type: TypeAlias = Literal[
    "OpenApi3",
    "JSONSchemaDraft4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OpenApi3",
        "JSONSchemaDraft4",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
