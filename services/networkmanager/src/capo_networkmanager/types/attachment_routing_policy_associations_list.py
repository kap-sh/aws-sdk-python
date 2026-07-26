"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentRoutingPolicyAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_routing_policy_association_summary

AttachmentRoutingPolicyAssociationsList: TypeAlias = list[
    "capo_networkmanager.types.attachment_routing_policy_association_summary.AttachmentRoutingPolicyAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentRoutingPolicyAssociationsList) -> list:
    import capo_networkmanager.types.attachment_routing_policy_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.attachment_routing_policy_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AttachmentRoutingPolicyAssociationsList:
    import capo_networkmanager.types.attachment_routing_policy_association_summary

    out: AttachmentRoutingPolicyAssociationsList = []
    for item in data:
        out.append(
            capo_networkmanager.types.attachment_routing_policy_association_summary.deserialize_json(
                item
            )
        )
    return out
