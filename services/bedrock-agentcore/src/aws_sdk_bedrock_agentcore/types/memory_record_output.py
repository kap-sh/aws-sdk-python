"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_id
    import aws_sdk_bedrock_agentcore.types.memory_record_status
    import aws_sdk_bedrock_agentcore.types.request_identifier


class MemoryRecordOutput(TypedDict, closed=True):
    memory_record_id: "aws_sdk_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique ID associated to the memory record.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.memory_record_status.MemoryRecordStatus"
    """<p>The status of the memory record operation (e.g., SUCCEEDED, FAILED).</p>"""
    request_identifier: NotRequired[
        "aws_sdk_bedrock_agentcore.types.request_identifier.RequestIdentifier"
    ]
    """<p>The client-provided identifier that was used to track this record operation.</p>"""
    error_code: NotRequired["int"]
    """<p>The error code returned when the memory record operation fails.</p>"""
    error_message: NotRequired["str"]
    """<p>A human-readable error message describing why the memory record operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordOutput) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    import aws_sdk_bedrock_agentcore.types.memory_record_status

    out["status"] = aws_sdk_bedrock_agentcore.types.memory_record_status.serialize_json(
        value["status"]
    )
    if "request_identifier" in value:
        out["requestIdentifier"] = value["request_identifier"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> MemoryRecordOutput:
    out: MemoryRecordOutput = {}  # type: ignore[typeddict-item]
    if "memoryRecordId" in data:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        raise DeserializationError("MemoryRecordOutput.memory_record_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("MemoryRecordOutput.status required")
    if "requestIdentifier" in data:
        out["request_identifier"] = data["requestIdentifier"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
