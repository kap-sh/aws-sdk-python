"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchCreateMemoryRecordsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_id
    import aws_sdk_bedrock_agentcore.types.memory_records_create_input_list


class BatchCreateMemoryRecordsInput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The unique ID of the memory resource where records will be created.</p>"""
    records: "aws_sdk_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList"
    """<p>A list of memory record creation inputs to be processed in the batch operation.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateMemoryRecordsInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_records_create_input_list

    out["records"] = (
        aws_sdk_bedrock_agentcore.types.memory_records_create_input_list.serialize_json(
            value["records"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchCreateMemoryRecordsInput:
    out: BatchCreateMemoryRecordsInput = {}  # type: ignore[typeddict-item]
    if "records" in data:
        import aws_sdk_bedrock_agentcore.types.memory_records_create_input_list

        out["records"] = (
            aws_sdk_bedrock_agentcore.types.memory_records_create_input_list.deserialize_json(
                data["records"]
            )
        )
    else:
        raise DeserializationError("BatchCreateMemoryRecordsInput.records required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
