"""Generated from Smithy shape ``com.amazonaws.inspector2#ListFindingAggregationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aggregation_request
    import aws_sdk_inspector2.types.aggregation_type
    import aws_sdk_inspector2.types.list_finding_aggregations_max_results
    import aws_sdk_inspector2.types.next_token
    import aws_sdk_inspector2.types.string_filter_list


class ListFindingAggregationsRequest(TypedDict, closed=True):
    aggregation_type: "aws_sdk_inspector2.types.aggregation_type.AggregationType"
    """<p>The type of the aggregation request.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired[
        "aws_sdk_inspector2.types.list_finding_aggregations_max_results.ListFindingAggregationsMaxResults"
    ]
    """<p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>"""
    account_ids: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The Amazon Web Services account IDs to retrieve finding aggregation data for.</p>"""
    aggregation_request: NotRequired[
        "aws_sdk_inspector2.types.aggregation_request.AggregationRequest"
    ]
    """<p>Details of the aggregation request that is used to filter your aggregation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingAggregationsRequest) -> dict:
    out: dict = {}
    out["aggregationType"] = value["aggregation_type"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "account_ids" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["accountIds"] = aws_sdk_inspector2.types.string_filter_list.serialize_json(
            value["account_ids"]
        )
    if "aggregation_request" in value:
        import aws_sdk_inspector2.types.aggregation_request

        out["aggregationRequest"] = (
            aws_sdk_inspector2.types.aggregation_request.serialize_json(
                value["aggregation_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListFindingAggregationsRequest:
    out: ListFindingAggregationsRequest = {}  # type: ignore[typeddict-item]
    if "aggregationType" in data:
        out["aggregation_type"] = data["aggregationType"]
    else:
        raise DeserializationError(
            "ListFindingAggregationsRequest.aggregation_type required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["accountIds"]
            )
        )
    if "aggregationRequest" in data:
        import aws_sdk_inspector2.types.aggregation_request

        out["aggregation_request"] = (
            aws_sdk_inspector2.types.aggregation_request.deserialize_json(
                data["aggregationRequest"]
            )
        )
    return out
