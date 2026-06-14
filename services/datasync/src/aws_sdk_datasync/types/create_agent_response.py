"""Generated from Smithy shape ``com.amazonaws.datasync#CreateAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn


class CreateAgentResponse(TypedDict):
    agent_arn: NotRequired["aws_sdk_datasync.types.agent_arn.AgentArn"]
    r"""<p>The ARN of the agent that you just activated. Use the <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/API_ListAgents.html\">ListAgents</a> operation to return a list of agents in your Amazon Web Services account and Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAgentResponse) -> dict:
    out: dict = {}
    if "agent_arn" in value:
        out["AgentArn"] = value["agent_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAgentResponse:
    out: CreateAgentResponse = {}  # type: ignore[typeddict-item]
    if "AgentArn" in data:
        out["agent_arn"] = data["AgentArn"]
    return out
