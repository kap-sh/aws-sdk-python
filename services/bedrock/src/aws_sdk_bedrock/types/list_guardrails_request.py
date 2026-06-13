"""Generated from Smithy shape ``com.amazonaws.bedrock#ListGuardrailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_identifier
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token


class ListGuardrailsRequest(TypedDict):
    guardrail_identifier: NotRequired[
        "aws_sdk_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    ]
    """<p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>"""
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If there are more results than were returned in the response, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGuardrailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGuardrailsRequest:
    out: ListGuardrailsRequest = {}  # type: ignore[typeddict-item]
    return out
