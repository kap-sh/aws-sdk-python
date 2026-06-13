"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_arn
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.agent_name
    import aws_sdk_quicksight.types.agent_status


class CreateAgentResponse(TypedDict):
    arn: "aws_sdk_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    agent_status: "aws_sdk_quicksight.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    agent_name: "aws_sdk_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import aws_sdk_quicksight.types.agent_status

    out["AgentStatus"] = aws_sdk_quicksight.types.agent_status.serialize_json(
        value["agent_status"]
    )
    out["AgentName"] = value["agent_name"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateAgentResponse:
    out: CreateAgentResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateAgentResponse.arn required")
    if "AgentId" in data:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("CreateAgentResponse.agent_id required")
    if "AgentStatus" in data:
        import aws_sdk_quicksight.types.agent_status

        out["agent_status"] = aws_sdk_quicksight.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    else:
        raise DeserializationError("CreateAgentResponse.agent_status required")
    if "AgentName" in data:
        out["agent_name"] = data["AgentName"]
    else:
        raise DeserializationError("CreateAgentResponse.agent_name required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
