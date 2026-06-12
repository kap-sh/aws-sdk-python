"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductTitleFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.saa_s_product_title_string

SaaSProductTitleFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.saa_s_product_title_string.SaaSProductTitleString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductTitleFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SaaSProductTitleFilterValueList:
    return list(data)
