"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.query_generation_column

QueryGenerationColumns: TypeAlias = list[
    "capo_bedrock_agent.types.query_generation_column.QueryGenerationColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationColumns) -> list:
    import capo_bedrock_agent.types.query_generation_column

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.query_generation_column.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QueryGenerationColumns:
    import capo_bedrock_agent.types.query_generation_column

    out: QueryGenerationColumns = []
    for item in data:
        out.append(
            capo_bedrock_agent.types.query_generation_column.deserialize_json(item)
        )
    return out
