"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItemClass``."""

from typing import Literal, TypeAlias, cast

CatalogItemClass: TypeAlias = Literal[
    "RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItemClass) -> str:
    return value


def deserialize_json(data: str) -> CatalogItemClass:
    return cast(CatalogItemClass, data)
