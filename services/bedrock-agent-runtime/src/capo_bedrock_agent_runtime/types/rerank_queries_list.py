"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankQueriesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.rerank_query

RerankQueriesList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.rerank_query.RerankQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: RerankQueriesList) -> list:
    import capo_bedrock_agent_runtime.types.rerank_query

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.rerank_query.serialize_json(item))
    return out


def deserialize_json(data: list) -> RerankQueriesList:
    import capo_bedrock_agent_runtime.types.rerank_query

    out: RerankQueriesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.rerank_query.deserialize_json(item))
    return out
