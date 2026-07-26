"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DescribeQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.query_alias
    import capo_cloudtrail.types.refresh_id
    import capo_cloudtrail.types.uuid


class DescribeQueryRequest(TypedDict, closed=True):
    event_data_store: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN (or the ID suffix of the ARN) of an event data store on which the specified query was run.</p>"""
    query_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p>The query ID.</p>"""
    query_alias: NotRequired["capo_cloudtrail.types.query_alias.QueryAlias"]
    """<p> The alias that identifies a query template. </p>"""
    refresh_id: NotRequired["capo_cloudtrail.types.refresh_id.RefreshId"]
    """<p> The ID of the dashboard refresh. </p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueryRequest) -> dict:
    out: dict = {}
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_alias" in value:
        out["QueryAlias"] = value["query_alias"]
    if "refresh_id" in value:
        out["RefreshId"] = value["refresh_id"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueryRequest:
    out: DescribeQueryRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "QueryAlias" in data:
        out["query_alias"] = data["QueryAlias"]
    if "RefreshId" in data:
        out["refresh_id"] = data["RefreshId"]
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
