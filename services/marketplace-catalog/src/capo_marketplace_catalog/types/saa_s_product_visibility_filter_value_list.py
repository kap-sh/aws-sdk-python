"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.saa_s_product_visibility_string

SaaSProductVisibilityFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.saa_s_product_visibility_string.SaaSProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductVisibilityFilterValueList) -> list:
    import capo_marketplace_catalog.types.saa_s_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.saa_s_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SaaSProductVisibilityFilterValueList:
    import capo_marketplace_catalog.types.saa_s_product_visibility_string

    out: SaaSProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            capo_marketplace_catalog.types.saa_s_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
