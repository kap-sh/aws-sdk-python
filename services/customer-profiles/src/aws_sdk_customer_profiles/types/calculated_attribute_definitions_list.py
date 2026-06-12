"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeDefinitionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_calculated_attribute_definition_item

CalculatedAttributeDefinitionsList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.list_calculated_attribute_definition_item.ListCalculatedAttributeDefinitionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeDefinitionsList) -> list:
    import aws_sdk_customer_profiles.types.list_calculated_attribute_definition_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.list_calculated_attribute_definition_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CalculatedAttributeDefinitionsList:
    import aws_sdk_customer_profiles.types.list_calculated_attribute_definition_item

    out: CalculatedAttributeDefinitionsList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.list_calculated_attribute_definition_item.deserialize_json(
                item
            )
        )
    return out
