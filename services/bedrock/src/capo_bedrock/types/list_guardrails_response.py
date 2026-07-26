"""Generated from Smithy shape ``com.amazonaws.bedrock#ListGuardrailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_summaries
    import capo_bedrock.types.pagination_token


class ListGuardrailsResponse(TypedDict, closed=True):
    guardrails: "capo_bedrock.types.guardrail_summaries.GuardrailSummaries"
    """<p>A list of objects, each of which contains details about a guardrail.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If there are more results than were returned in the response, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGuardrailsResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.guardrail_summaries

    out["guardrails"] = capo_bedrock.types.guardrail_summaries.serialize_json(
        value["guardrails"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGuardrailsResponse:
    out: ListGuardrailsResponse = {}  # type: ignore[typeddict-item]
    if "guardrails" in data:
        import capo_bedrock.types.guardrail_summaries

        out["guardrails"] = capo_bedrock.types.guardrail_summaries.deserialize_json(
            data["guardrails"]
        )
    else:
        raise DeserializationError("ListGuardrailsResponse.guardrails required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
