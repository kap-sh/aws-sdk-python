"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DefinitionType``."""

from typing import Literal, TypeAlias, cast

DefinitionType: TypeAlias = Literal[
    "WORKLOAD_METADATA",
    "APP_REGISTRY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefinitionType) -> str:
    return value


def deserialize_json(data: str) -> DefinitionType:
    return cast(DefinitionType, data)
