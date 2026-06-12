"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchByAttributeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.search_by_attribute_value

SearchByAttributeValues: TypeAlias = list[
    "aws_sdk_medical_imaging.types.search_by_attribute_value.SearchByAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchByAttributeValues) -> list:
    import aws_sdk_medical_imaging.types.search_by_attribute_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medical_imaging.types.search_by_attribute_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchByAttributeValues:
    import aws_sdk_medical_imaging.types.search_by_attribute_value

    out: SearchByAttributeValues = []
    for item in data:
        out.append(
            aws_sdk_medical_imaging.types.search_by_attribute_value.deserialize_json(
                item
            )
        )
    return out
