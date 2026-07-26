"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_state
    import capo_networkmanager.types.attachment_type
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListAttachmentsRequest(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    attachment_type: NotRequired[
        "capo_networkmanager.types.attachment_type.AttachmentType"
    ]
    """<p>The type of attachment.</p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Region where the edge is located.</p>"""
    state: NotRequired["capo_networkmanager.types.attachment_state.AttachmentState"]
    """<p>The state of the attachment.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttachmentsRequest:
    out: ListAttachmentsRequest = {}  # type: ignore[typeddict-item]
    return out
