"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.boolean
    import aws_sdk_application_discovery_service.types.string


class AgentConfigurationStatus(TypedDict, closed=True):
    agent_id: NotRequired["aws_sdk_application_discovery_service.types.string.String"]
    """<p>The agent ID.</p>"""
    operation_succeeded: "aws_sdk_application_discovery_service.types.boolean.Boolean"
    """<p>Information about the status of the <code>StartDataCollection</code> and <code>StopDataCollection</code> operations. The system has recorded the data collection operation. The agent receives this command the next time it polls for a new command. </p>"""
    description: NotRequired[
        "aws_sdk_application_discovery_service.types.string.String"
    ]
    """<p>A description of the operation performed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentConfigurationStatus) -> dict:
    out: dict = {}
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    out["operationSucceeded"] = value.get("operation_succeeded", False)
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentConfigurationStatus:
    out: AgentConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    if "operationSucceeded" in data:
        out["operation_succeeded"] = data["operationSucceeded"]
    else:
        out["operation_succeeded"] = False
    if "description" in data:
        out["description"] = data["description"]
    return out
