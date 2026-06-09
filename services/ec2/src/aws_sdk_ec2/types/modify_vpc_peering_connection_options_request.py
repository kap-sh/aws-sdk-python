"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcPeeringConnectionOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.peering_connection_options_request
    import aws_sdk_ec2.types.vpc_peering_connection_id


class ModifyVpcPeeringConnectionOptionsRequest(TypedDict):
    accepter_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options_request.PeeringConnectionOptionsRequest"
    ]
    """<p>The VPC peering connection options for the accepter VPC.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    requester_peering_connection_options: NotRequired[
        "aws_sdk_ec2.types.peering_connection_options_request.PeeringConnectionOptionsRequest"
    ]
    """<p>The VPC peering connection options for the requester VPC.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_id.VpcPeeringConnectionId"
    ]
    """<p>The ID of the VPC peering connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcPeeringConnectionOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "accepter_peering_connection_options" in value:
        import aws_sdk_ec2.types.peering_connection_options_request

        aws_sdk_ec2.types.peering_connection_options_request.serialize_ec2_query(
            value["accepter_peering_connection_options"],
            pairs,
            f"{prefix}.AccepterPeeringConnectionOptions",
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "requester_peering_connection_options" in value:
        import aws_sdk_ec2.types.peering_connection_options_request

        aws_sdk_ec2.types.peering_connection_options_request.serialize_ec2_query(
            value["requester_peering_connection_options"],
            pairs,
            f"{prefix}.RequesterPeeringConnectionOptions",
        )
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcPeeringConnectionOptionsRequest:
    out: ModifyVpcPeeringConnectionOptionsRequest = {}  # type: ignore[typeddict-item]
    child_accepter_peering_connection_options = el.find(
        "AccepterPeeringConnectionOptions"
    )
    if child_accepter_peering_connection_options is not None:
        import aws_sdk_ec2.types.peering_connection_options_request

        out["accepter_peering_connection_options"] = (
            aws_sdk_ec2.types.peering_connection_options_request.deserialize_ec2_query(
                child_accepter_peering_connection_options
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_requester_peering_connection_options = el.find(
        "RequesterPeeringConnectionOptions"
    )
    if child_requester_peering_connection_options is not None:
        import aws_sdk_ec2.types.peering_connection_options_request

        out["requester_peering_connection_options"] = (
            aws_sdk_ec2.types.peering_connection_options_request.deserialize_ec2_query(
                child_requester_peering_connection_options
            )
        )
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    return out
