"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ListConnectInstanceIntegrationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.instance_id
    import aws_sdk_connectcampaignsv2.types.max_results
    import aws_sdk_connectcampaignsv2.types.next_token


class ListConnectInstanceIntegrationsRequest(TypedDict):
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    max_results: NotRequired["aws_sdk_connectcampaignsv2.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_connectcampaignsv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectInstanceIntegrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectInstanceIntegrationsRequest:
    out: ListConnectInstanceIntegrationsRequest = {}  # type: ignore[typeddict-item]
    return out
