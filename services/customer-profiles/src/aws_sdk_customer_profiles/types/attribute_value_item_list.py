"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeValueItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_value_item

AttributeValueItemList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.attribute_value_item.AttributeValueItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueItemList) -> list:
    import aws_sdk_customer_profiles.types.attribute_value_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.attribute_value_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttributeValueItemList:
    import aws_sdk_customer_profiles.types.attribute_value_item

    out: AttributeValueItemList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.attribute_value_item.deserialize_json(item)
        )
    return out
