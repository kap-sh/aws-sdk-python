"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankSourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.rerank_source

RerankSourcesList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.rerank_source.RerankSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankSourcesList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.rerank_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.rerank_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RerankSourcesList:
    import aws_sdk_bedrock_agent_runtime.types.rerank_source

    out: RerankSourcesList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.rerank_source.deserialize_json(item)
        )
    return out
