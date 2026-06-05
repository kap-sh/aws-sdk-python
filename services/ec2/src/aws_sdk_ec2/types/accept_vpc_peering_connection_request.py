"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcPeeringConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpc_peering_connection_id_with_resolver


class AcceptVpcPeeringConnectionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_id_with_resolver.VpcPeeringConnectionIdWithResolver"
    ]
    """<p>The ID of the VPC peering connection. You must specify this parameter in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptVpcPeeringConnectionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> AcceptVpcPeeringConnectionRequest:
    out: AcceptVpcPeeringConnectionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    return out
