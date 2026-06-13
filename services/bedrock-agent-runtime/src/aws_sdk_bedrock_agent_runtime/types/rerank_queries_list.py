"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankQueriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.rerank_query

RerankQueriesList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.rerank_query.RerankQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankQueriesList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.rerank_query

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.rerank_query.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RerankQueriesList:
    import aws_sdk_bedrock_agent_runtime.types.rerank_query

    out: RerankQueriesList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.rerank_query.deserialize_json(item)
        )
    return out
