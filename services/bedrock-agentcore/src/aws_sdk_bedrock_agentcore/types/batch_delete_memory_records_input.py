"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchDeleteMemoryRecordsInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list

class BatchDeleteMemoryRecordsInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be deleted.</p>"""
    records: "aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList"
    """<p>A list of memory record deletion inputs to be processed in the batch operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteMemoryRecordsInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list
    out["records"] = aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list.serialize_json(value["records"])
    return out


def deserialize_json(data: dict) -> BatchDeleteMemoryRecordsInput:
    out: BatchDeleteMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if "records" in data:
        import aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list
        out["records"] = aws_sdk_bedrock_agentcore.types.memory_records_delete_input_list.deserialize_json(data["records"])
    else:
        raise DeserializationError("BatchDeleteMemoryRecordsInput.records required")
    return out