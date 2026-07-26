"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connection_id_list
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class GetConnectionsRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    connection_ids: NotRequired[
        "capo_networkmanager.types.connection_id_list.ConnectionIdList"
    ]
    """<p>One or more connection IDs.</p>"""
    device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectionsRequest:
    out: GetConnectionsRequest = {}  # type: ignore[typeddict-item]
    return out
