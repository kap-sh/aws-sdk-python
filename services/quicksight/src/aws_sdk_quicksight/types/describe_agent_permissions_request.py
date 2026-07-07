"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAgentPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.aws_account_id


class DescribeAgentPermissionsRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAgentPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAgentPermissionsRequest:
    out: DescribeAgentPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
