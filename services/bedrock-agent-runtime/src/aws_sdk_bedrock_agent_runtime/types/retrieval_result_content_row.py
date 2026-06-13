"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column

RetrievalResultContentRow: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column.RetrievalResultContentColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultContentRow) -> list:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RetrievalResultContentRow:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column

    out: RetrievalResultContentRow = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_content_column.deserialize_json(
                item
            )
        )
    return out
