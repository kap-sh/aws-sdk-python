"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayVpcAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.create_transit_gateway_vpc_attachment_request_options
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_gateway_id
    import capo_ec2.types.transit_gateway_subnet_id_list
    import capo_ec2.types.vpc_id


class CreateTransitGatewayVpcAttachmentRequest(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    subnet_ids: NotRequired[
        "capo_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.</p>"""
    options: NotRequired[
        "capo_ec2.types.create_transit_gateway_vpc_attachment_request_options.CreateTransitGatewayVpcAttachmentRequestOptions"
    ]
    """<p>The VPC attachment options.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the VPC attachment.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayVpcAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "subnet_ids" in value:
        import capo_ec2.types.transit_gateway_subnet_id_list

        capo_ec2.types.transit_gateway_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIds"
        )
    if "options" in value:
        import capo_ec2.types.create_transit_gateway_vpc_attachment_request_options

        capo_ec2.types.create_transit_gateway_vpc_attachment_request_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayVpcAttachmentRequest:
    out: CreateTransitGatewayVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_ids = el.find("SubnetIds")
    if child_subnet_ids is not None:
        import capo_ec2.types.transit_gateway_subnet_id_list

        out["subnet_ids"] = (
            capo_ec2.types.transit_gateway_subnet_id_list.deserialize_ec2_query(
                child_subnet_ids
            )
        )
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.create_transit_gateway_vpc_attachment_request_options

        out["options"] = (
            capo_ec2.types.create_transit_gateway_vpc_attachment_request_options.deserialize_ec2_query(
                child_options
            )
        )
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
