"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentRoutingPolicyAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.constrained_string_list


class AttachmentRoutingPolicyAssociationSummary(TypedDict, closed=True):
    attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the attachment associated with the routing policy.</p>"""
    pending_routing_policies: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The list of routing policies that are pending association with the attachment.</p>"""
    associated_routing_policies: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The list of routing policies currently associated with the attachment.</p>"""
    routing_policy_label: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label associated with the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentRoutingPolicyAssociationSummary) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "pending_routing_policies" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["PendingRoutingPolicies"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["pending_routing_policies"]
            )
        )
    if "associated_routing_policies" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["AssociatedRoutingPolicies"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["associated_routing_policies"]
            )
        )
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    return out


def deserialize_json(data: dict) -> AttachmentRoutingPolicyAssociationSummary:
    out: AttachmentRoutingPolicyAssociationSummary = {}  # type: ignore[typeddict-item]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "PendingRoutingPolicies" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["pending_routing_policies"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["PendingRoutingPolicies"]
            )
        )
    if "AssociatedRoutingPolicies" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["associated_routing_policies"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["AssociatedRoutingPolicies"]
            )
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    return out
