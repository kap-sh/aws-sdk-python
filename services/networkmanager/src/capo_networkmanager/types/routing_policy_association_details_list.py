"""Generated from Smithy shape ``com.amazonaws.networkmanager#RoutingPolicyAssociationDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.routing_policy_association_detail

RoutingPolicyAssociationDetailsList: TypeAlias = list[
    "capo_networkmanager.types.routing_policy_association_detail.RoutingPolicyAssociationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingPolicyAssociationDetailsList) -> list:
    import capo_networkmanager.types.routing_policy_association_detail

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.routing_policy_association_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RoutingPolicyAssociationDetailsList:
    import capo_networkmanager.types.routing_policy_association_detail

    out: RoutingPolicyAssociationDetailsList = []
    for item in data:
        out.append(
            capo_networkmanager.types.routing_policy_association_detail.deserialize_json(
                item
            )
        )
    return out
