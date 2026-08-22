"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TraceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.trace_id

TraceIds: TypeAlias = list["capo_bedrock_agentcore.types.trace_id.TraceId"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> TraceIds:
    return [item for item in data if item is not None]
