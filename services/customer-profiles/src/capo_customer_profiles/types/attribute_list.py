"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_item

AttributeList: TypeAlias = list[
    "capo_customer_profiles.types.attribute_item.AttributeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeList) -> list:
    import capo_customer_profiles.types.attribute_item

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.attribute_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeList:
    import capo_customer_profiles.types.attribute_item

    out: AttributeList = []
    for item in data:
        out.append(capo_customer_profiles.types.attribute_item.deserialize_json(item))
    return out
