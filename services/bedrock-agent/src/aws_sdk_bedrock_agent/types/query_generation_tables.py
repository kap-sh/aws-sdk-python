"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationTables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.query_generation_table

QueryGenerationTables: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.query_generation_table.QueryGenerationTable"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationTables) -> list:
    import aws_sdk_bedrock_agent.types.query_generation_table

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.query_generation_table.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QueryGenerationTables:
    import aws_sdk_bedrock_agent.types.query_generation_table

    out: QueryGenerationTables = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.query_generation_table.deserialize_json(item)
        )
    return out
