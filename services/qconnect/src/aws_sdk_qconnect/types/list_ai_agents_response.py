"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIAgentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_summary_list
    import aws_sdk_qconnect.types.next_token


class ListAIAgentsResponse(TypedDict):
    ai_agent_summaries: (
        "aws_sdk_qconnect.types.ai_agent_summary_list.AIAgentSummaryList"
    )
    """<p>The summaries of AI Agents.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIAgentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.ai_agent_summary_list

    out["aiAgentSummaries"] = (
        aws_sdk_qconnect.types.ai_agent_summary_list.serialize_json(
            value["ai_agent_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIAgentsResponse:
    out: ListAIAgentsResponse = {}  # type: ignore[typeddict-item]
    if "aiAgentSummaries" in data:
        import aws_sdk_qconnect.types.ai_agent_summary_list

        out["ai_agent_summaries"] = (
            aws_sdk_qconnect.types.ai_agent_summary_list.deserialize_json(
                data["aiAgentSummaries"]
            )
        )
    else:
        raise DeserializationError("ListAIAgentsResponse.ai_agent_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
