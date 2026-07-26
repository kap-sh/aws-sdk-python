"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductTitleFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.container_product_title_string

ContainerProductTitleFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.container_product_title_string.ContainerProductTitleString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductTitleFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ContainerProductTitleFilterValueList:
    return list(data)
