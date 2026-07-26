"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListAttachmentRoutingPolicyAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_routing_policy_associations_list
    import capo_networkmanager.types.next_token


class ListAttachmentRoutingPolicyAssociationsResponse(TypedDict, closed=True):
    attachment_routing_policy_associations: NotRequired[
        "capo_networkmanager.types.attachment_routing_policy_associations_list.AttachmentRoutingPolicyAssociationsList"
    ]
    """<p>The list of attachment routing policy associations.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachmentRoutingPolicyAssociationsResponse) -> dict:
    out: dict = {}
    if "attachment_routing_policy_associations" in value:
        import capo_networkmanager.types.attachment_routing_policy_associations_list

        out["AttachmentRoutingPolicyAssociations"] = (
            capo_networkmanager.types.attachment_routing_policy_associations_list.serialize_json(
                value["attachment_routing_policy_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttachmentRoutingPolicyAssociationsResponse:
    out: ListAttachmentRoutingPolicyAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "AttachmentRoutingPolicyAssociations" in data:
        import capo_networkmanager.types.attachment_routing_policy_associations_list

        out["attachment_routing_policy_associations"] = (
            capo_networkmanager.types.attachment_routing_policy_associations_list.deserialize_json(
                data["AttachmentRoutingPolicyAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
