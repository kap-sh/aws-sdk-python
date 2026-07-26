"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributesForProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_calculated_attribute_for_profile_item

CalculatedAttributesForProfileList: TypeAlias = list[
    "capo_customer_profiles.types.list_calculated_attribute_for_profile_item.ListCalculatedAttributeForProfileItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributesForProfileList) -> list:
    import capo_customer_profiles.types.list_calculated_attribute_for_profile_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_calculated_attribute_for_profile_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CalculatedAttributesForProfileList:
    import capo_customer_profiles.types.list_calculated_attribute_for_profile_item

    out: CalculatedAttributesForProfileList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.list_calculated_attribute_for_profile_item.deserialize_json(
                item
            )
        )
    return out
