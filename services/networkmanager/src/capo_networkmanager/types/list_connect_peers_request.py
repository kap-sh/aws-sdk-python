"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListConnectPeersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListConnectPeersRequest(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    connect_attachment_id: NotRequired[
        "capo_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectPeersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectPeersRequest:
    out: ListConnectPeersRequest = {}  # type: ignore[typeddict-item]
    return out
