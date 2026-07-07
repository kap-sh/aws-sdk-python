"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BatchDeleteMemoryRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_records_output_list


class BatchDeleteMemoryRecordsOutput(TypedDict, closed=True):
    successful_records: "aws_sdk_bedrock_agentcore.types.memory_records_output_list.MemoryRecordsOutputList"
    """<p>A list of memory records that were successfully deleted during the batch operation.</p>"""
    failed_records: "aws_sdk_bedrock_agentcore.types.memory_records_output_list.MemoryRecordsOutputList"
    """<p>A list of memory records that failed to be deleted, including error details for each failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteMemoryRecordsOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_records_output_list

    out["successfulRecords"] = (
        aws_sdk_bedrock_agentcore.types.memory_records_output_list.serialize_json(
            value["successful_records"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.memory_records_output_list

    out["failedRecords"] = (
        aws_sdk_bedrock_agentcore.types.memory_records_output_list.serialize_json(
            value["failed_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteMemoryRecordsOutput:
    out: BatchDeleteMemoryRecordsOutput = {}  # type: ignore[typeddict-item]
    if "successfulRecords" in data:
        import aws_sdk_bedrock_agentcore.types.memory_records_output_list

        out["successful_records"] = (
            aws_sdk_bedrock_agentcore.types.memory_records_output_list.deserialize_json(
                data["successfulRecords"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteMemoryRecordsOutput.successful_records required"
        )
    if "failedRecords" in data:
        import aws_sdk_bedrock_agentcore.types.memory_records_output_list

        out["failed_records"] = (
            aws_sdk_bedrock_agentcore.types.memory_records_output_list.deserialize_json(
                data["failedRecords"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteMemoryRecordsOutput.failed_records required"
        )
    return out
