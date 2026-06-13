"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.generated_query

GeneratedQueries: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.generated_query.GeneratedQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedQueries) -> list:
    import aws_sdk_bedrock_agent_runtime.types.generated_query

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.generated_query.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GeneratedQueries:
    import aws_sdk_bedrock_agent_runtime.types.generated_query

    out: GeneratedQueries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.generated_query.deserialize_json(item)
        )
    return out
