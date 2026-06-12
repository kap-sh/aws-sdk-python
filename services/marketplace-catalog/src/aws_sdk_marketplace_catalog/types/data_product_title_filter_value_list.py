"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductTitleFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.data_product_title_string

DataProductTitleFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.data_product_title_string.DataProductTitleString"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductTitleFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DataProductTitleFilterValueList:
    return list(data)
