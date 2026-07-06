"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcPeeringConnectionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_peering_connection


class AcceptVpcPeeringConnectionResult(TypedDict, closed=True):
    vpc_peering_connection: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection.VpcPeeringConnection"
    ]
    """<p>Information about the VPC peering connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptVpcPeeringConnectionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_peering_connection" in value:
        import aws_sdk_ec2.types.vpc_peering_connection

        aws_sdk_ec2.types.vpc_peering_connection.serialize_ec2_query(
            value["vpc_peering_connection"], pairs, f"{prefix}.VpcPeeringConnection"
        )


def deserialize_ec2_query(el: Element) -> AcceptVpcPeeringConnectionResult:
    out: AcceptVpcPeeringConnectionResult = {}  # type: ignore[typeddict-item]
    child_vpc_peering_connection = el.find("VpcPeeringConnection")
    if child_vpc_peering_connection is not None:
        import aws_sdk_ec2.types.vpc_peering_connection

        out["vpc_peering_connection"] = (
            aws_sdk_ec2.types.vpc_peering_connection.deserialize_ec2_query(
                child_vpc_peering_connection
            )
        )
    return out
