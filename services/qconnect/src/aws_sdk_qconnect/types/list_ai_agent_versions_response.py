"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIAgentVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_version_summaries_list
    import aws_sdk_qconnect.types.next_token


class ListAIAgentVersionsResponse(TypedDict):
    ai_agent_version_summaries: "aws_sdk_qconnect.types.ai_agent_version_summaries_list.AIAgentVersionSummariesList"
    """<p>The summaries of AI Agent versions.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIAgentVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.ai_agent_version_summaries_list

    out["aiAgentVersionSummaries"] = (
        aws_sdk_qconnect.types.ai_agent_version_summaries_list.serialize_json(
            value["ai_agent_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIAgentVersionsResponse:
    out: ListAIAgentVersionsResponse = {}  # type: ignore[typeddict-item]
    if "aiAgentVersionSummaries" in data:
        import aws_sdk_qconnect.types.ai_agent_version_summaries_list

        out["ai_agent_version_summaries"] = (
            aws_sdk_qconnect.types.ai_agent_version_summaries_list.deserialize_json(
                data["aiAgentVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAIAgentVersionsResponse.ai_agent_version_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
