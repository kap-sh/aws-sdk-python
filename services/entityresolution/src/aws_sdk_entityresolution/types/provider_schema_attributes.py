"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderSchemaAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.provider_schema_attribute

ProviderSchemaAttributes: TypeAlias = list[
    "aws_sdk_entityresolution.types.provider_schema_attribute.ProviderSchemaAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderSchemaAttributes) -> list:
    import aws_sdk_entityresolution.types.provider_schema_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.provider_schema_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProviderSchemaAttributes:
    import aws_sdk_entityresolution.types.provider_schema_attribute

    out: ProviderSchemaAttributes = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.provider_schema_attribute.deserialize_json(
                item
            )
        )
    return out
