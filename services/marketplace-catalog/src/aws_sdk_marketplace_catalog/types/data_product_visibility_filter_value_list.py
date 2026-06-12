"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductVisibilityFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.data_product_visibility_string

DataProductVisibilityFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.data_product_visibility_string.DataProductVisibilityString"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductVisibilityFilterValueList) -> list:
    import aws_sdk_marketplace_catalog.types.data_product_visibility_string

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_catalog.types.data_product_visibility_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataProductVisibilityFilterValueList:
    import aws_sdk_marketplace_catalog.types.data_product_visibility_string

    out: DataProductVisibilityFilterValueList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_catalog.types.data_product_visibility_string.deserialize_json(
                item
            )
        )
    return out
