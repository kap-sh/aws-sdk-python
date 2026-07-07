"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.agent_arn


class DescribeAgentRequest(TypedDict, closed=True):
    agent_arn: "aws_sdk_datasync.types.agent_arn.AgentArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the DataSync agent that you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgentRequest) -> dict:
    out: dict = {}
    out["AgentArn"] = value["agent_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgentRequest:
    out: DescribeAgentRequest = {}  # type: ignore[typeddict-item]
    if "AgentArn" in data:
        out["agent_arn"] = data["AgentArn"]
    else:
        raise DeserializationError("DescribeAgentRequest.agent_arn required")
    return out
