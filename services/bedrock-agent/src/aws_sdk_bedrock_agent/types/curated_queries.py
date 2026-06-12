"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CuratedQueries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.curated_query

CuratedQueries: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.curated_query.CuratedQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: CuratedQueries) -> list:
    import aws_sdk_bedrock_agent.types.curated_query

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.curated_query.serialize_json(item))
    return out


def deserialize_json(data: list) -> CuratedQueries:
    import aws_sdk_bedrock_agent.types.curated_query

    out: CuratedQueries = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.curated_query.deserialize_json(item))
    return out
