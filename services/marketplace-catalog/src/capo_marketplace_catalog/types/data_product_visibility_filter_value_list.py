"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.data_product_visibility_string

DataProductVisibilityFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.data_product_visibility_string.DataProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductVisibilityFilterValueList) -> list:
    import capo_marketplace_catalog.types.data_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.data_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataProductVisibilityFilterValueList:
    import capo_marketplace_catalog.types.data_product_visibility_string

    out: DataProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.data_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
