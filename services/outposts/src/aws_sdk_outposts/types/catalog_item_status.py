"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItemStatus``."""

from typing import Literal, TypeAlias, cast

CatalogItemStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DISCONTINUED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItemStatus) -> str:
    return value


def deserialize_json(data: str) -> CatalogItemStatus:
    return cast(CatalogItemStatus, data)
