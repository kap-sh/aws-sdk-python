"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.max_results
    import capo_wisdom.types.next_token
    import capo_wisdom.types.search_expression
    import capo_wisdom.types.uuid_or_arn


class SearchSessionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_wisdom.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    search_expression: "capo_wisdom.types.search_expression.SearchExpression"
    """<p>The search expression to filter results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSessionsRequest) -> dict:
    out: dict = {}
    import capo_wisdom.types.search_expression

    out["searchExpression"] = capo_wisdom.types.search_expression.serialize_json(
        value["search_expression"]
    )
    return out


def deserialize_json(data: dict) -> SearchSessionsRequest:
    out: SearchSessionsRequest = {}  # type: ignore[typeddict-item]
    if "searchExpression" in data:
        import capo_wisdom.types.search_expression

        out["search_expression"] = capo_wisdom.types.search_expression.deserialize_json(
            data["searchExpression"]
        )
    else:
        raise DeserializationError("SearchSessionsRequest.search_expression required")
    return out
