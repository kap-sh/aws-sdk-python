"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.rerank_result

RerankResultsList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.rerank_result.RerankResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankResultsList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.rerank_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.rerank_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RerankResultsList:
    import aws_sdk_bedrock_agent_runtime.types.rerank_result

    out: RerankResultsList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.rerank_result.deserialize_json(item)
        )
    return out
