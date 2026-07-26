"""Generated from Smithy shape ``com.amazonaws.appsync#TypeDefinitionFormat``."""

from typing import Literal, TypeAlias, cast

TypeDefinitionFormat: TypeAlias = Literal[
    "SDL",
    "JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: TypeDefinitionFormat) -> str:
    return value


def deserialize_json(data: str) -> TypeDefinitionFormat:
    return cast(TypeDefinitionFormat, data)
