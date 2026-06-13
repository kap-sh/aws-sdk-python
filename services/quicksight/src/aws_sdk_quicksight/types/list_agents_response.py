"""Generated from Smithy shape ``com.amazonaws.quicksight#ListAgentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_summaries


class ListAgentsResponse(TypedDict):
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    agent_summaries: "aws_sdk_quicksight.types.agent_summaries.AgentSummaries"
    """<p>A list of agent summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    import aws_sdk_quicksight.types.agent_summaries

    out["AgentSummaries"] = aws_sdk_quicksight.types.agent_summaries.serialize_json(
        value["agent_summaries"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentsResponse:
    out: ListAgentsResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "AgentSummaries" in data:
        import aws_sdk_quicksight.types.agent_summaries

        out["agent_summaries"] = (
            aws_sdk_quicksight.types.agent_summaries.deserialize_json(
                data["AgentSummaries"]
            )
        )
    else:
        raise DeserializationError("ListAgentsResponse.agent_summaries required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
