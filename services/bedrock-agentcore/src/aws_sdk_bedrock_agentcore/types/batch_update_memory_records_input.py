"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchUpdateMemoryRecordsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.memory_records_update_input_list


class BatchUpdateMemoryRecordsInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be updated.</p>"""
    records: "aws_sdk_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList"
    """<p>A list of memory record update inputs to be processed in the batch operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateMemoryRecordsInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_records_update_input_list

    out["records"] = (
        aws_sdk_bedrock_agentcore.types.memory_records_update_input_list.serialize_json(
            value["records"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateMemoryRecordsInput:
    out: BatchUpdateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if "records" in data:
        import aws_sdk_bedrock_agentcore.types.memory_records_update_input_list

        out["records"] = (
            aws_sdk_bedrock_agentcore.types.memory_records_update_input_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateMemoryRecordsInput.records required")
    return out
