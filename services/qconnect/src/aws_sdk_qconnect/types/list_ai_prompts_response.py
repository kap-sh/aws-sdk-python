"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIPromptsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_summary_list
    import aws_sdk_qconnect.types.next_token


class ListAIPromptsResponse(TypedDict, closed=True):
    ai_prompt_summaries: (
        "aws_sdk_qconnect.types.ai_prompt_summary_list.AIPromptSummaryList"
    )
    """<p>The summaries of the AI Prompts.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIPromptsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.ai_prompt_summary_list

    out["aiPromptSummaries"] = (
        aws_sdk_qconnect.types.ai_prompt_summary_list.serialize_json(
            value["ai_prompt_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIPromptsResponse:
    out: ListAIPromptsResponse = {}  # type: ignore[typeddict-item]
    if "aiPromptSummaries" in data:
        import aws_sdk_qconnect.types.ai_prompt_summary_list

        out["ai_prompt_summaries"] = (
            aws_sdk_qconnect.types.ai_prompt_summary_list.deserialize_json(
                data["aiPromptSummaries"]
            )
        )
    else:
        raise DeserializationError("ListAIPromptsResponse.ai_prompt_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
