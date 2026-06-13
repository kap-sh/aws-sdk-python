"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_filter

RetrievalFilterList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.retrieval_filter.RetrievalFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalFilterList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.retrieval_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievalFilterList:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_filter

    out: RetrievalFilterList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.retrieval_filter.deserialize_json(item)
        )
    return out
