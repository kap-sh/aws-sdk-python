"""Generated from Smithy shape ``com.amazonaws.outposts#CatalogItemClassList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.catalog_item_class

CatalogItemClassList: TypeAlias = list[
    "capo_outposts.types.catalog_item_class.CatalogItemClass"
]


# --- restJson1 ser/de ---
def serialize_json(value: CatalogItemClassList) -> list:
    import capo_outposts.types.catalog_item_class

    out: list = []
    for item in value:
        out.append(capo_outposts.types.catalog_item_class.serialize_json(item))
    return out


def deserialize_json(data: list) -> CatalogItemClassList:
    import capo_outposts.types.catalog_item_class

    out: CatalogItemClassList = []
    for item in data:
        out.append(capo_outposts.types.catalog_item_class.deserialize_json(item))
    return out
