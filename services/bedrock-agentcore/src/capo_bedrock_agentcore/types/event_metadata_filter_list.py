"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventMetadataFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.event_metadata_filter_expression

EventMetadataFilterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.event_metadata_filter_expression.EventMetadataFilterExpression"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventMetadataFilterList) -> list:
    import capo_bedrock_agentcore.types.event_metadata_filter_expression

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.event_metadata_filter_expression.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EventMetadataFilterList:
    import capo_bedrock_agentcore.types.event_metadata_filter_expression

    out: EventMetadataFilterList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.event_metadata_filter_expression.deserialize_json(
                item
            )
        )
    return out
