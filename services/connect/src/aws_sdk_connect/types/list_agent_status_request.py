"""Generated from Smithy shape ``com.amazonaws.connect#ListAgentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_types
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token


class ListAgentStatusRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page.</p>"""
    agent_status_types: NotRequired[
        "aws_sdk_connect.types.agent_status_types.AgentStatusTypes"
    ]
    """<p>Available agent status types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentStatusRequest:
    out: ListAgentStatusRequest = {}  # type: ignore[typeddict-item]
    return out
