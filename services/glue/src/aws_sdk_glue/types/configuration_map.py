"""Generated from Smithy shape ``com.amazonaws.glue#ConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.configuration_object
    import aws_sdk_glue.types.name_string

ConfigurationMap: TypeAlias = dict[
    "aws_sdk_glue.types.name_string.NameString",
    "aws_sdk_glue.types.configuration_object.ConfigurationObject",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_glue.types.configuration_object

        out[key] = aws_sdk_glue.types.configuration_object.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationMap:
    out: ConfigurationMap = {}
    for key, value in data.items():
        import aws_sdk_glue.types.configuration_object

        out[key] = aws_sdk_glue.types.configuration_object.deserialize_aws_json_1_1(
            value
        )
    return out
