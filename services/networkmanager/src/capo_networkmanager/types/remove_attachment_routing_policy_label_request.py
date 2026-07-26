"""Generated from Smithy shape ``com.amazonaws.networkmanager#RemoveAttachmentRoutingPolicyLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.core_network_id


class RemoveAttachmentRoutingPolicyLabelRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network containing the attachment.</p>"""
    attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment to remove the routing policy label from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAttachmentRoutingPolicyLabelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveAttachmentRoutingPolicyLabelRequest:
    out: RemoveAttachmentRoutingPolicyLabelRequest = {}  # type: ignore[typeddict-item]
    return out
