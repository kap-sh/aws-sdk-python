"""Generated from Smithy shape ``com.amazonaws.forecast#SchemaAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.schema_attribute

SchemaAttributes: TypeAlias = list[
    "aws_sdk_forecast.types.schema_attribute.SchemaAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaAttributes) -> list:
    import aws_sdk_forecast.types.schema_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_forecast.types.schema_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SchemaAttributes:
    import aws_sdk_forecast.types.schema_attribute

    out: SchemaAttributes = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.schema_attribute.deserialize_aws_json_1_1(item)
        )
    return out
