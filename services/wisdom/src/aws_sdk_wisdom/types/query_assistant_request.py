"""Generated from Smithy shape ``com.amazonaws.wisdom#QueryAssistantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.max_results
    import aws_sdk_wisdom.types.next_token
    import aws_sdk_wisdom.types.query_text
    import aws_sdk_wisdom.types.uuid_or_arn


class QueryAssistantRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    query_text: "aws_sdk_wisdom.types.query_text.QueryText"
    """<p>The text to search for.</p>"""
    next_token: NotRequired["aws_sdk_wisdom.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryAssistantRequest) -> dict:
    out: dict = {}
    out["queryText"] = value["query_text"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> QueryAssistantRequest:
    out: QueryAssistantRequest = {}  # type: ignore[typeddict-item]
    if "queryText" in data:
        out["query_text"] = data["queryText"]
    else:
        raise DeserializationError("QueryAssistantRequest.query_text required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
