"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieval_result_content_column

RetrievalResultContentRow: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.retrieval_result_content_column.RetrievalResultContentColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultContentRow) -> list:
    import capo_bedrock_agent_runtime.types.retrieval_result_content_column

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.retrieval_result_content_column.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RetrievalResultContentRow:
    import capo_bedrock_agent_runtime.types.retrieval_result_content_column

    out: RetrievalResultContentRow = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.retrieval_result_content_column.deserialize_json(
                item
            )
        )
    return out
