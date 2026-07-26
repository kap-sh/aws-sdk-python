"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.container_product_visibility_string

ContainerProductVisibilityFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.container_product_visibility_string.ContainerProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductVisibilityFilterValueList) -> list:
    import capo_marketplace_catalog.types.container_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.container_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContainerProductVisibilityFilterValueList:
    import capo_marketplace_catalog.types.container_product_visibility_string

    out: ContainerProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.container_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
