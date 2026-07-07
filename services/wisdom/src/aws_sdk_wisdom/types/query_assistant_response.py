"""Generated from Smithy shape ``com.amazonaws.wisdom#QueryAssistantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.next_token
    import aws_sdk_wisdom.types.query_results_list


class QueryAssistantResponse(TypedDict, closed=True):
    results: "aws_sdk_wisdom.types.query_results_list.QueryResultsList"
    """<p>The results of the query.</p>"""
    next_token: NotRequired["aws_sdk_wisdom.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryAssistantResponse) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.query_results_list

    out["results"] = aws_sdk_wisdom.types.query_results_list.serialize_json(
        value["results"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> QueryAssistantResponse:
    out: QueryAssistantResponse = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_wisdom.types.query_results_list

        out["results"] = aws_sdk_wisdom.types.query_results_list.deserialize_json(
            data["results"]
        )
    else:
        raise DeserializationError("QueryAssistantResponse.results required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
