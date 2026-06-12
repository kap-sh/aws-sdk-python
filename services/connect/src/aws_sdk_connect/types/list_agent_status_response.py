"""Generated from Smithy shape ``com.amazonaws.connect#ListAgentStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_status_summary_list
    import aws_sdk_connect.types.next_token


class ListAgentStatusResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    agent_status_summary_list: NotRequired[
        "aws_sdk_connect.types.agent_status_summary_list.AgentStatusSummaryList"
    ]
    """<p>A summary of agent statuses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentStatusResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "agent_status_summary_list" in value:
        import aws_sdk_connect.types.agent_status_summary_list

        out["AgentStatusSummaryList"] = (
            aws_sdk_connect.types.agent_status_summary_list.serialize_json(
                value["agent_status_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAgentStatusResponse:
    out: ListAgentStatusResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AgentStatusSummaryList" in data:
        import aws_sdk_connect.types.agent_status_summary_list

        out["agent_status_summary_list"] = (
            aws_sdk_connect.types.agent_status_summary_list.deserialize_json(
                data["AgentStatusSummaryList"]
            )
        )
    return out
