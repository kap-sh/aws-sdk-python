"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.filter_value_content

ValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.filter_value_content.FilterValueContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValueList:
    return list(data)
