"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SpanIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.span_id

SpanIds: TypeAlias = list["aws_sdk_bedrock_agentcore.types.span_id.SpanId"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SpanIds:
    return list(data)
