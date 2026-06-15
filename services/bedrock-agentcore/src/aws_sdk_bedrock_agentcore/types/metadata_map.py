"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.metadata_key
    import aws_sdk_bedrock_agentcore.types.metadata_value

MetadataMap: TypeAlias = dict[
    "aws_sdk_bedrock_agentcore.types.metadata_key.MetadataKey",
    "aws_sdk_bedrock_agentcore.types.metadata_value.MetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_agentcore.types.metadata_value

        out[key] = aws_sdk_bedrock_agentcore.types.metadata_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MetadataMap:
    out: MetadataMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_agentcore.types.metadata_value

        out[key] = aws_sdk_bedrock_agentcore.types.metadata_value.deserialize_json(
            value
        )
    return out
