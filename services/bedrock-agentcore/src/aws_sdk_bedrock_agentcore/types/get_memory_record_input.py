"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetMemoryRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.memory_record_id


class GetMemoryRecordInput(TypedDict, closed=True):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource containing the memory record.</p>"""
    memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The identifier of the memory record to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemoryRecordInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMemoryRecordInput:
    out: GetMemoryRecordInput = {}  # type: ignore[typeddict-item]
    return out
