"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.query_generation_column

QueryGenerationColumns: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.query_generation_column.QueryGenerationColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationColumns) -> list:
    import aws_sdk_bedrock_agent.types.query_generation_column

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.query_generation_column.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QueryGenerationColumns:
    import aws_sdk_bedrock_agent.types.query_generation_column

    out: QueryGenerationColumns = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.query_generation_column.deserialize_json(item)
        )
    return out
