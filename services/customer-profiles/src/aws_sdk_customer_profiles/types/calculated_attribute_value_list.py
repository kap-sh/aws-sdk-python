"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.calculated_attribute_value

CalculatedAttributeValueList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.calculated_attribute_value.CalculatedAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedAttributeValueList) -> list:
    import aws_sdk_customer_profiles.types.calculated_attribute_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.calculated_attribute_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CalculatedAttributeValueList:
    import aws_sdk_customer_profiles.types.calculated_attribute_value

    out: CalculatedAttributeValueList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.calculated_attribute_value.deserialize_json(
                item
            )
        )
    return out
