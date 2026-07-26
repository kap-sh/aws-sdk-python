"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItemListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.catalog_item

CatalogItemListDefinition: TypeAlias = list[
    "capo_outposts.types.catalog_item.CatalogItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItemListDefinition) -> list:
    import capo_outposts.types.catalog_item

    out: list = []
    for item in value:
        out.append(capo_outposts.types.catalog_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> CatalogItemListDefinition:
    import capo_outposts.types.catalog_item

    out: CatalogItemListDefinition = []
    for item in data:
        out.append(capo_outposts.types.catalog_item.deserialize_json(item))
    return out
