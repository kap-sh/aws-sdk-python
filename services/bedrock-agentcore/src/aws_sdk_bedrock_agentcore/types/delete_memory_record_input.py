"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteMemoryRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.memory_record_id


class DeleteMemoryRecordInput(TypedDict, closed=True):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource from which to delete the memory record.</p>"""
    memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The identifier of the memory record to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryRecordInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMemoryRecordInput:
    out: DeleteMemoryRecordInput = {}  # type: ignore[typeddict-item]
    return out
