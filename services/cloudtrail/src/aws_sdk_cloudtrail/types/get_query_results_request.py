"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetQueryResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.account_id
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.max_query_results
    import aws_sdk_cloudtrail.types.pagination_token
    import aws_sdk_cloudtrail.types.uuid


class GetQueryResultsRequest(TypedDict, closed=True):
    event_data_store: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN (or ID suffix of the ARN) of the event data store against which the query was run.</p>"""
    query_id: "aws_sdk_cloudtrail.types.uuid.UUID"
    """<p>The ID of the query for which you want to get results.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of query results.</p>"""
    max_query_results: NotRequired[
        "aws_sdk_cloudtrail.types.max_query_results.MaxQueryResults"
    ]
    """<p>The maximum number of query results to display on a single page.</p>"""
    event_data_store_owner_account_id: NotRequired[
        "aws_sdk_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryResultsRequest) -> dict:
    out: dict = {}
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    out["QueryId"] = value["query_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_query_results" in value:
        out["MaxQueryResults"] = value["max_query_results"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryResultsRequest:
    out: GetQueryResultsRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("GetQueryResultsRequest.query_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxQueryResults" in data:
        out["max_query_results"] = data["MaxQueryResults"]
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
