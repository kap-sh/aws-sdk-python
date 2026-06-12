"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListObjectTypeAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_object_type_attribute_item

ListObjectTypeAttributesList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.list_object_type_attribute_item.ListObjectTypeAttributeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListObjectTypeAttributesList) -> list:
    import aws_sdk_customer_profiles.types.list_object_type_attribute_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.list_object_type_attribute_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListObjectTypeAttributesList:
    import aws_sdk_customer_profiles.types.list_object_type_attribute_item

    out: ListObjectTypeAttributesList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.list_object_type_attribute_item.deserialize_json(
                item
            )
        )
    return out
