"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection_id_list
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token


class GetConnectionsRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    connection_ids: NotRequired[
        "aws_sdk_networkmanager.types.connection_id_list.ConnectionIdList"
    ]
    """<p>One or more connection IDs.</p>"""
    device_id: NotRequired["aws_sdk_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectionsRequest:
    out: GetConnectionsRequest = {}  # type: ignore[typeddict-item]
    return out
