"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributesForProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_calculated_attribute_for_profile_item

CalculatedAttributesForProfileList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.list_calculated_attribute_for_profile_item.ListCalculatedAttributeForProfileItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributesForProfileList) -> list:
    import aws_sdk_customer_profiles.types.list_calculated_attribute_for_profile_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.list_calculated_attribute_for_profile_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CalculatedAttributesForProfileList:
    import aws_sdk_customer_profiles.types.list_calculated_attribute_for_profile_item

    out: CalculatedAttributesForProfileList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.list_calculated_attribute_for_profile_item.deserialize_json(
                item
            )
        )
    return out
