"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SecurityGroupReference(TypedDict, closed=True):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of your security group.</p>"""
    referencing_vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC with the referencing security group.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>The ID of the VPC peering connection (if applicable). For more information about security group referencing for peering connections, see <a href=\"https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-security-groups.html\">Update your security groups to reference peer security groups</a> in the <i>VPC Peering Guide</i>.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway (if applicable).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupReference, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "referencing_vpc_id" in value:
        pairs.append((f"{prefix}.ReferencingVpcId", str(value["referencing_vpc_id"])))
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))


def deserialize_ec2_query(el: Element) -> SecurityGroupReference:
    out: SecurityGroupReference = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_referencing_vpc_id = el.find("ReferencingVpcId")
    if child_referencing_vpc_id is not None:
        out["referencing_vpc_id"] = str(child_referencing_vpc_id.text or "")
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    return out
