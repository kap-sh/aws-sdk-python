"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryMetadataFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_expression

MemoryMetadataFilterList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.memory_metadata_filter_expression.MemoryMetadataFilterExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryMetadataFilterList) -> list:
    import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_expression

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_metadata_filter_expression.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemoryMetadataFilterList:
    import aws_sdk_bedrock_agentcore.types.memory_metadata_filter_expression

    out: MemoryMetadataFilterList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.memory_metadata_filter_expression.deserialize_json(
                item
            )
        )
    return out
