"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent


class DescribeAgentResponse(TypedDict, closed=True):
    agent: "aws_sdk_quicksight.types.agent.Agent"
    """<p>The full details of the agent, including its configuration, status, and associations.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentResponse) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.agent

    out["Agent"] = aws_sdk_quicksight.types.agent.serialize_json(value["agent"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAgentResponse:
    out: DescribeAgentResponse = {}  # type: ignore[typeddict-item]
    if "Agent" in data:
        import aws_sdk_quicksight.types.agent

        out["agent"] = aws_sdk_quicksight.types.agent.deserialize_json(data["Agent"])
    else:
        raise DeserializationError("DescribeAgentResponse.agent required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
