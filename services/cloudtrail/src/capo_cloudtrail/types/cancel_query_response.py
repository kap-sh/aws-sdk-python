"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CancelQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.query_status
    import capo_cloudtrail.types.uuid


class CancelQueryResponse(TypedDict, closed=True):
    query_id: "capo_cloudtrail.types.uuid.UUID"
    """<p>The ID of the canceled query.</p>"""
    query_status: "capo_cloudtrail.types.query_status.QueryStatus"
    """<p>Shows the status of a query after a <code>CancelQuery</code> request. Typically, the values shown are either <code>RUNNING</code> or <code>CANCELLED</code>.</p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelQueryResponse) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    import capo_cloudtrail.types.query_status

    out["QueryStatus"] = capo_cloudtrail.types.query_status.serialize_aws_json_1_1(
        value["query_status"]
    )
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelQueryResponse:
    out: CancelQueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("CancelQueryResponse.query_id required")
    if "QueryStatus" in data:
        import capo_cloudtrail.types.query_status

        out["query_status"] = (
            capo_cloudtrail.types.query_status.deserialize_aws_json_1_1(
                data["QueryStatus"]
            )
        )
    else:
        raise DeserializationError("CancelQueryResponse.query_status required")
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
