"""Generated from Smithy shape ``com.amazonaws.glue#PropertyTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.property_type

PropertyTypes: TypeAlias = list["capo_glue.types.property_type.PropertyType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PropertyTypes) -> list:
    import capo_glue.types.property_type

    out: list = []
    for item in value:
        out.append(capo_glue.types.property_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PropertyTypes:
    import capo_glue.types.property_type

    out: PropertyTypes = []
    for item in data:
        out.append(capo_glue.types.property_type.deserialize_aws_json_1_1(item))
    return out
