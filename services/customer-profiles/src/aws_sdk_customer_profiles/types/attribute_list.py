"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_item

AttributeList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.attribute_item.AttributeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeList) -> list:
    import aws_sdk_customer_profiles.types.attribute_item

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.attribute_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeList:
    import aws_sdk_customer_profiles.types.attribute_item

    out: AttributeList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.attribute_item.deserialize_json(item)
        )
    return out
