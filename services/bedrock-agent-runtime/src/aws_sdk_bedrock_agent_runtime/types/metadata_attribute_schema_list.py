"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MetadataAttributeSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema

MetadataAttributeSchemaList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema.MetadataAttributeSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeSchemaList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetadataAttributeSchemaList:
    import aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema

    out: MetadataAttributeSchemaList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema.deserialize_json(
                item
            )
        )
    return out
