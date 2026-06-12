"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.saa_s_product_visibility_string

SaaSProductVisibilityFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.saa_s_product_visibility_string.SaaSProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductVisibilityFilterValueList) -> list:
    import aws_sdk_marketplace_catalog.types.saa_s_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_catalog.types.saa_s_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SaaSProductVisibilityFilterValueList:
    import aws_sdk_marketplace_catalog.types.saa_s_product_visibility_string

    out: SaaSProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_catalog.types.saa_s_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
