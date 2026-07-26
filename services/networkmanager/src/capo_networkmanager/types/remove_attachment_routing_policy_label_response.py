"""Generated from Smithy shape ``com.amazonaws.networkmanager#RemoveAttachmentRoutingPolicyLabelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id


class RemoveAttachmentRoutingPolicyLabelResponse(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of the core network containing the attachment.</p>"""
    attachment_id: NotRequired["capo_networkmanager.types.attachment_id.AttachmentId"]
    """<p>The ID of the attachment from which the routing policy label was removed.</p>"""
    routing_policy_label: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label that was removed from the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveAttachmentRoutingPolicyLabelResponse) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    return out


def deserialize_json(data: dict) -> RemoveAttachmentRoutingPolicyLabelResponse:
    out: RemoveAttachmentRoutingPolicyLabelResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    return out
