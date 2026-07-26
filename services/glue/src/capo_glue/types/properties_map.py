"""Generated from Smithy shape ``com.amazonaws.glue#PropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.property
    import capo_glue.types.property_name

PropertiesMap: TypeAlias = dict[
    "capo_glue.types.property_name.PropertyName", "capo_glue.types.property.Property"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.property

        out[key] = capo_glue.types.property.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PropertiesMap:
    out: PropertiesMap = {}
    for key, value in data.items():
        import capo_glue.types.property

        out[key] = capo_glue.types.property.deserialize_aws_json_1_1(value)
    return out
