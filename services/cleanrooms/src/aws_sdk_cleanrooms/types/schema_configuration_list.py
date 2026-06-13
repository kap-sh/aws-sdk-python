"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.schema_configuration

SchemaConfigurationList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.schema_configuration.SchemaConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaConfigurationList) -> list:
    import aws_sdk_cleanrooms.types.schema_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.schema_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaConfigurationList:
    import aws_sdk_cleanrooms.types.schema_configuration

    out: SchemaConfigurationList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.schema_configuration.deserialize_json(item))
    return out
