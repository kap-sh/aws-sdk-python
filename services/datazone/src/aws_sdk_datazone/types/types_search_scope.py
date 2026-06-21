"""Generated from Smithy shape ``com.amazonaws.datazone#TypesSearchScope``."""

from typing import Literal, TypeAlias, cast

TypesSearchScope: TypeAlias = Literal[
    "ASSET_TYPE",
    "FORM_TYPE",
    "LINEAGE_NODE_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TypesSearchScope) -> str:
    return value


def deserialize_json(data: str) -> TypesSearchScope:
    return cast(TypesSearchScope, data)
