"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIPromptVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_version_summaries_list
    import aws_sdk_qconnect.types.next_token


class ListAIPromptVersionsResponse(TypedDict, closed=True):
    ai_prompt_version_summaries: "aws_sdk_qconnect.types.ai_prompt_version_summaries_list.AIPromptVersionSummariesList"
    """<p>The summaries of the AI Prompt versions.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIPromptVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.ai_prompt_version_summaries_list

    out["aiPromptVersionSummaries"] = (
        aws_sdk_qconnect.types.ai_prompt_version_summaries_list.serialize_json(
            value["ai_prompt_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIPromptVersionsResponse:
    out: ListAIPromptVersionsResponse = {}  # type: ignore[typeddict-item]
    if "aiPromptVersionSummaries" in data:
        import aws_sdk_qconnect.types.ai_prompt_version_summaries_list

        out["ai_prompt_version_summaries"] = (
            aws_sdk_qconnect.types.ai_prompt_version_summaries_list.deserialize_json(
                data["aiPromptVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAIPromptVersionsResponse.ai_prompt_version_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
