"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.calculated_attribute_value

CalculatedAttributeValueList: TypeAlias = list[
    "capo_customer_profiles.types.calculated_attribute_value.CalculatedAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeValueList) -> list:
    import capo_customer_profiles.types.calculated_attribute_value

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.calculated_attribute_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CalculatedAttributeValueList:
    import capo_customer_profiles.types.calculated_attribute_value

    out: CalculatedAttributeValueList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.calculated_attribute_value.deserialize_json(
                item
            )
        )
    return out
