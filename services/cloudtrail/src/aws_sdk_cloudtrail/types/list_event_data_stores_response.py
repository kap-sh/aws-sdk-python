"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListEventDataStoresResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_stores
    import aws_sdk_cloudtrail.types.pagination_token


class ListEventDataStoresResponse(TypedDict):
    event_data_stores: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_stores.EventDataStores"
    ]
    """<p>Contains information about event data stores in the account, in the current Region.</p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p>A token you can use to get the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventDataStoresResponse) -> dict:
    out: dict = {}
    if "event_data_stores" in value:
        import aws_sdk_cloudtrail.types.event_data_stores

        out["EventDataStores"] = (
            aws_sdk_cloudtrail.types.event_data_stores.serialize_aws_json_1_1(
                value["event_data_stores"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventDataStoresResponse:
    out: ListEventDataStoresResponse = {}  # type: ignore[typeddict-item]
    if "EventDataStores" in data:
        import aws_sdk_cloudtrail.types.event_data_stores

        out["event_data_stores"] = (
            aws_sdk_cloudtrail.types.event_data_stores.deserialize_aws_json_1_1(
                data["EventDataStores"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
