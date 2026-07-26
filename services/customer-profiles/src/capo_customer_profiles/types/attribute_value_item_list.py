"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeValueItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_value_item

AttributeValueItemList: TypeAlias = list[
    "capo_customer_profiles.types.attribute_value_item.AttributeValueItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValueItemList) -> list:
    import capo_customer_profiles.types.attribute_value_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.attribute_value_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AttributeValueItemList:
    import capo_customer_profiles.types.attribute_value_item

    out: AttributeValueItemList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.attribute_value_item.deserialize_json(item)
        )
    return out
