"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.metadata_attribute

MetadataAttributes: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.metadata_attribute.MetadataAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributes) -> list:
    import aws_sdk_bedrock_agent.types.metadata_attribute

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.metadata_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataAttributes:
    import aws_sdk_bedrock_agent.types.metadata_attribute

    out: MetadataAttributes = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.metadata_attribute.deserialize_json(item)
        )
    return out
