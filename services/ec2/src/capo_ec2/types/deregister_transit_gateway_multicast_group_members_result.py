"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupMembersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_deregistered_group_members


class DeregisterTransitGatewayMulticastGroupMembersResult(TypedDict, closed=True):
    deregistered_multicast_group_members: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_deregistered_group_members.TransitGatewayMulticastDeregisteredGroupMembers"
    ]
    """<p>Information about the deregistered members.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterTransitGatewayMulticastGroupMembersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "deregistered_multicast_group_members" in value:
        import capo_ec2.types.transit_gateway_multicast_deregistered_group_members

        capo_ec2.types.transit_gateway_multicast_deregistered_group_members.serialize_ec2_query(
            value["deregistered_multicast_group_members"],
            pairs,
            f"{key_prefix}DeregisteredMulticastGroupMembers",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeregisterTransitGatewayMulticastGroupMembersResult:
    out: DeregisterTransitGatewayMulticastGroupMembersResult = {}  # type: ignore[typeddict-item]
    child_deregistered_multicast_group_members = el.find(
        "DeregisteredMulticastGroupMembers"
    )
    if child_deregistered_multicast_group_members is not None:
        import capo_ec2.types.transit_gateway_multicast_deregistered_group_members

        out["deregistered_multicast_group_members"] = (
            capo_ec2.types.transit_gateway_multicast_deregistered_group_members.deserialize_ec2_query(
                child_deregistered_multicast_group_members
            )
        )
    return out
