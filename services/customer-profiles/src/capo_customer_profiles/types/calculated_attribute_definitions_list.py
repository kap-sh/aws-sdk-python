"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeDefinitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_calculated_attribute_definition_item

CalculatedAttributeDefinitionsList: TypeAlias = list[
    "capo_customer_profiles.types.list_calculated_attribute_definition_item.ListCalculatedAttributeDefinitionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeDefinitionsList) -> list:
    import capo_customer_profiles.types.list_calculated_attribute_definition_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_calculated_attribute_definition_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CalculatedAttributeDefinitionsList:
    import capo_customer_profiles.types.list_calculated_attribute_definition_item

    out: CalculatedAttributeDefinitionsList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.list_calculated_attribute_definition_item.deserialize_json(
                item
            )
        )
    return out
