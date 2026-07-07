"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CancelQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.account_id
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.uuid


class CancelQueryRequest(TypedDict, closed=True):
    event_data_store: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN (or the ID suffix of the ARN) of an event data store on which the specified query is running.</p>"""
    query_id: "aws_sdk_cloudtrail.types.uuid.UUID"
    """<p>The ID of the query that you want to cancel. The <code>QueryId</code> comes from the response of a <code>StartQuery</code> operation.</p>"""
    event_data_store_owner_account_id: NotRequired[
        "aws_sdk_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelQueryRequest) -> dict:
    out: dict = {}
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    out["QueryId"] = value["query_id"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelQueryRequest:
    out: CancelQueryRequest = {}  # type: ignore[typeddict-item]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("CancelQueryRequest.query_id required")
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
