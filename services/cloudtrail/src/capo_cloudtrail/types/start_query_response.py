"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.uuid


class StartQueryResponse(TypedDict, closed=True):
    query_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p>The ID of the started query.</p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQueryResponse) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQueryResponse:
    out: StartQueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
