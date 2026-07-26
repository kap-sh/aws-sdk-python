"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.ami_product_visibility_string

AmiProductVisibilityFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.ami_product_visibility_string.AmiProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductVisibilityFilterValueList) -> list:
    import capo_marketplace_catalog.types.ami_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.ami_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AmiProductVisibilityFilterValueList:
    import capo_marketplace_catalog.types.ami_product_visibility_string

    out: AmiProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.ami_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
