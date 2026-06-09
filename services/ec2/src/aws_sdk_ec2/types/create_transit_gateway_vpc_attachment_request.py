"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_subnet_id_list
    import aws_sdk_ec2.types.vpc_id


class CreateTransitGatewayVpcAttachmentRequest(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options.CreateTransitGatewayVpcAttachmentRequestOptions"
    ]
    """<p>The VPC attachment options.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the VPC attachment.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayVpcAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "subnet_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        aws_sdk_ec2.types.transit_gateway_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "options" in value:
        import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options

        aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayVpcAttachmentRequest:
    out: CreateTransitGatewayVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    if el.find("SubnetIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_ec2.types.transit_gateway_subnet_id_list.deserialize_ec2_query(
                el, "SubnetIds"
            )
        )
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options

        out["options"] = (
            aws_sdk_ec2.types.create_transit_gateway_vpc_attachment_request_options.deserialize_ec2_query(
                child_options
            )
        )
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
