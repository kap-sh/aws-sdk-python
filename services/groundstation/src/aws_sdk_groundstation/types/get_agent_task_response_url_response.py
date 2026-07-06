"""Generated from Smithy shape ``com.amazonaws.groundstation#GetAgentTaskResponseUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class GetAgentTaskResponseUrlResponse(TypedDict, closed=True):
    agent_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of the agent.</p>"""
    task_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>GUID of the agent task.</p>"""
    presigned_log_url: "str"
    """<p>Presigned URL for uploading agent task response logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentTaskResponseUrlResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["taskId"] = value["task_id"]
    out["presignedLogUrl"] = value["presigned_log_url"]
    return out


def deserialize_json(data: dict) -> GetAgentTaskResponseUrlResponse:
    out: GetAgentTaskResponseUrlResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("GetAgentTaskResponseUrlResponse.agent_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("GetAgentTaskResponseUrlResponse.task_id required")
    if "presignedLogUrl" in data:
        out["presigned_log_url"] = data["presignedLogUrl"]
    else:
        raise DeserializationError(
            "GetAgentTaskResponseUrlResponse.presigned_log_url required"
        )
    return out
