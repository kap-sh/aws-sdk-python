"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIGuardrailVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_version_summaries_list
    import aws_sdk_qconnect.types.next_token


class ListAIGuardrailVersionsResponse(TypedDict):
    ai_guardrail_version_summaries: "aws_sdk_qconnect.types.ai_guardrail_version_summaries_list.AIGuardrailVersionSummariesList"
    """<p>The summaries of the AI Guardrail versions.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIGuardrailVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.ai_guardrail_version_summaries_list

    out["aiGuardrailVersionSummaries"] = (
        aws_sdk_qconnect.types.ai_guardrail_version_summaries_list.serialize_json(
            value["ai_guardrail_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIGuardrailVersionsResponse:
    out: ListAIGuardrailVersionsResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrailVersionSummaries" in data:
        import aws_sdk_qconnect.types.ai_guardrail_version_summaries_list

        out["ai_guardrail_version_summaries"] = (
            aws_sdk_qconnect.types.ai_guardrail_version_summaries_list.deserialize_json(
                data["aiGuardrailVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAIGuardrailVersionsResponse.ai_guardrail_version_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
