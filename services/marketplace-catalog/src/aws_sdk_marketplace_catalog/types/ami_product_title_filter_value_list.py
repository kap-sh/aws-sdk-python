"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AmiProductTitleFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.ami_product_title_string

AmiProductTitleFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.ami_product_title_string.AmiProductTitleString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AmiProductTitleFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> AmiProductTitleFilterValueList:
    return list(data)
