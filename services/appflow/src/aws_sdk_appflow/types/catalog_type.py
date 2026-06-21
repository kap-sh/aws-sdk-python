"""Generated from Smithy shape ``com.amazonaws.appflow#CatalogType``."""

from typing import Literal, TypeAlias, cast

CatalogType: TypeAlias = Literal["GLUE",]


# --- restJson1 ser/de ---
def serialize_json(value: CatalogType) -> str:
    return value


def deserialize_json(data: str) -> CatalogType:
    return cast(CatalogType, data)
