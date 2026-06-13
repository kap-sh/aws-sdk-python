"""Generated from Smithy shape ``com.amazonaws.qconnect#ListAIGuardrailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_guardrail_summaries_list
    import aws_sdk_qconnect.types.next_token


class ListAIGuardrailsResponse(TypedDict):
    ai_guardrail_summaries: (
        "aws_sdk_qconnect.types.ai_guardrail_summaries_list.AIGuardrailSummariesList"
    )
    """<p>The summaries of the AI Guardrails.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAIGuardrailsResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.ai_guardrail_summaries_list

    out["aiGuardrailSummaries"] = (
        aws_sdk_qconnect.types.ai_guardrail_summaries_list.serialize_json(
            value["ai_guardrail_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAIGuardrailsResponse:
    out: ListAIGuardrailsResponse = {}  # type: ignore[typeddict-item]
    if "aiGuardrailSummaries" in data:
        import aws_sdk_qconnect.types.ai_guardrail_summaries_list

        out["ai_guardrail_summaries"] = (
            aws_sdk_qconnect.types.ai_guardrail_summaries_list.deserialize_json(
                data["aiGuardrailSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAIGuardrailsResponse.ai_guardrail_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
