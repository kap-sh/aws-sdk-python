"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableVpcAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.vpc_id


class CreateLocalGatewayRouteTableVpcAssociationRequest(TypedDict):
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the local gateway route table VPC association.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLocalGatewayRouteTableVpcAssociationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> CreateLocalGatewayRouteTableVpcAssociationRequest:
    out: CreateLocalGatewayRouteTableVpcAssociationRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
