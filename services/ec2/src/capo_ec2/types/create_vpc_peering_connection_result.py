"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcPeeringConnectionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_peering_connection


class CreateVpcPeeringConnectionResult(TypedDict, closed=True):
    vpc_peering_connection: NotRequired[
        "capo_ec2.types.vpc_peering_connection.VpcPeeringConnection"
    ]
    """<p>Information about the VPC peering connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcPeeringConnectionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_peering_connection" in value:
        import capo_ec2.types.vpc_peering_connection

        capo_ec2.types.vpc_peering_connection.serialize_ec2_query(
            value["vpc_peering_connection"], pairs, f"{key_prefix}VpcPeeringConnection"
        )


def deserialize_ec2_query(el: Element) -> CreateVpcPeeringConnectionResult:
    out: CreateVpcPeeringConnectionResult = {}  # type: ignore[typeddict-item]
    child_vpc_peering_connection = el.find("VpcPeeringConnection")
    if child_vpc_peering_connection is not None:
        import capo_ec2.types.vpc_peering_connection

        out["vpc_peering_connection"] = (
            capo_ec2.types.vpc_peering_connection.deserialize_ec2_query(
                child_vpc_peering_connection
            )
        )
    return out
