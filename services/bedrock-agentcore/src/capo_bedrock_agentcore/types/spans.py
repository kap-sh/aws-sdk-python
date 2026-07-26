"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Spans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.span

Spans: TypeAlias = list["capo_bedrock_agentcore.types.span.Span"]


# --- restJson1 ser/de ---
def serialize_json(value: Spans) -> list:
    return list(value)


def deserialize_json(data: list) -> Spans:
    return list(data)
