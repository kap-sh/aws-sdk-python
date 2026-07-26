"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIGuardrailVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_version_summaries_list
    import capo_qconnect.types.next_token


class ListAIGuardrailVersionsResponse(TypedDict, closed=True):
    ai_guardrail_version_summaries: "capo_qconnect.types.ai_guardrail_version_summaries_list.AIGuardrailVersionSummariesList"
    """<p>The summaries of the AI Guardrail versions.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIGuardrailVersionsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.ai_guardrail_version_summaries_list

    out["aiGuardrailVersionSummaries"] = (
        capo_qconnect.types.ai_guardrail_version_summaries_list.serialize_json(
            value["ai_guardrail_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIGuardrailVersionsResponse:
    out: ListAIGuardrailVersionsResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrailVersionSummaries" in data:
        import capo_qconnect.types.ai_guardrail_version_summaries_list

        out["ai_guardrail_version_summaries"] = (
            capo_qconnect.types.ai_guardrail_version_summaries_list.deserialize_json(
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
