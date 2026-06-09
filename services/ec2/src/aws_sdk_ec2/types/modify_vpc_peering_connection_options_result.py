"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcPeeringConnectionOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.peering_connection_options


class ModifyVpcPeeringConnectionOptionsResult(TypedDict):
    accepter_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options.PeeringConnectionOptions"
    ]
    """<p>Information about the VPC peering connection options for the accepter VPC.</p>"""
    requester_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options.PeeringConnectionOptions"
    ]
    """<p>Information about the VPC peering connection options for the requester VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcPeeringConnectionOptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "accepter_peering_connection_options" in value:
        import aws_sdk_ec2.types.peering_connection_options

        aws_sdk_ec2.types.peering_connection_options.serialize_ec2_query(
            value["accepter_peering_connection_options"],
            pairs,
            f"{prefix}.AccepterPeeringConnectionOptions",
        )
    if "requester_peering_connection_options" in value:
        import aws_sdk_ec2.types.peering_connection_options

        aws_sdk_ec2.types.peering_connection_options.serialize_ec2_query(
            value["requester_peering_connection_options"],
            pairs,
            f"{prefix}.RequesterPeeringConnectionOptions",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcPeeringConnectionOptionsResult:
    out: ModifyVpcPeeringConnectionOptionsResult = {}  # type: ignore[typeddict-item]
    child_accepter_peering_connection_options = el.find(
        "AccepterPeeringConnectionOptions"
    )
    if child_accepter_peering_connection_options is not None:
        import aws_sdk_ec2.types.peering_connection_options

        out["accepter_peering_connection_options"] = (
            aws_sdk_ec2.types.peering_connection_options.deserialize_ec2_query(
                child_accepter_peering_connection_options
            )
        )
    child_requester_peering_connection_options = el.find(
        "RequesterPeeringConnectionOptions"
    )
    if child_requester_peering_connection_options is not None:
        import aws_sdk_ec2.types.peering_connection_options

        out["requester_peering_connection_options"] = (
            aws_sdk_ec2.types.peering_connection_options.deserialize_ec2_query(
                child_requester_peering_connection_options
            )
        )
    return out
