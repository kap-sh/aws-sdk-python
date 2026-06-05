"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupMembersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members


class RegisterTransitGatewayMulticastGroupMembersResult(TypedDict):
    registered_multicast_group_members: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members.TransitGatewayMulticastRegisteredGroupMembers"
    ]
    """<p>Information about the registered transit gateway multicast group members.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisterTransitGatewayMulticastGroupMembersResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "registered_multicast_group_members" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members

        aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members.serialize_ec2_query(
            value["registered_multicast_group_members"],
            pairs,
            f"{prefix}.RegisteredMulticastGroupMembers",
        )


def deserialize_ec2_query(
    el: Element,
) -> RegisterTransitGatewayMulticastGroupMembersResult:
    out: RegisterTransitGatewayMulticastGroupMembersResult = {}  # type: ignore[typeddict-item]
    child_registered_multicast_group_members = el.find(
        "RegisteredMulticastGroupMembers"
    )
    if child_registered_multicast_group_members is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members

        out["registered_multicast_group_members"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members.deserialize_ec2_query(
                child_registered_multicast_group_members
            )
        )
    return out
