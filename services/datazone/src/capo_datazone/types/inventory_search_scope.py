"""Generated from Smithy shape ``com.amazonaws.datazone#InventorySearchScope``."""

from typing import Literal, TypeAlias, cast

InventorySearchScope: TypeAlias = Literal[
    "ASSET",
    "GLOSSARY",
    "GLOSSARY_TERM",
    "DATA_PRODUCT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InventorySearchScope) -> str:
    return value


def deserialize_json(data: str) -> InventorySearchScope:
    return cast(InventorySearchScope, data)
