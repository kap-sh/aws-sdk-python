"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationExceptionPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.property_validation_exception_property

PropertyValidationExceptionPropertyList: TypeAlias = list[
    "aws_sdk_connect.types.property_validation_exception_property.PropertyValidationExceptionProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValidationExceptionPropertyList) -> list:
    import aws_sdk_connect.types.property_validation_exception_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.property_validation_exception_property.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PropertyValidationExceptionPropertyList:
    import aws_sdk_connect.types.property_validation_exception_property

    out: PropertyValidationExceptionPropertyList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.property_validation_exception_property.deserialize_json(
                item
            )
        )
    return out
