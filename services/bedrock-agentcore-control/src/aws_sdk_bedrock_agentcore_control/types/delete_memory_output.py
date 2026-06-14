"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteMemoryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory_id
    import aws_sdk_bedrock_agentcore_control.types.memory_status


class DeleteMemoryOutput(TypedDict):
    memory_id: "aws_sdk_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the deleted AgentCore Memory resource.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.memory_status.MemoryStatus"
    ]
    """<p>The current status of the AgentCore Memory resource deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryOutput) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    if "status" in value:
        import aws_sdk_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteMemoryOutput:
    out: DeleteMemoryOutput = {}  # type: ignore[typeddict-item]
    if "memoryId" in data:
        out["memory_id"] = data["memoryId"]
    else:
        raise DeserializationError("DeleteMemoryOutput.memory_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_status.deserialize_json(
                data["status"]
            )
        )
    return out
