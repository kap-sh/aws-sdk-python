"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_subnet_id_list


class ModifyTransitGatewayVpcAttachmentRequest(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    add_subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets to add. You can specify at most one subnet per Availability Zone.</p>"""
    remove_subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of one or more subnets to remove.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options.ModifyTransitGatewayVpcAttachmentRequestOptions"
    ]
    """<p>The new VPC attachment options.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayVpcAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "add_subnet_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        aws_sdk_ec2.types.transit_gateway_subnet_id_list.serialize_ec2_query(
            value["add_subnet_ids"], pairs, f"{prefix}.AddSubnetIds"
        )
    if "remove_subnet_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        aws_sdk_ec2.types.transit_gateway_subnet_id_list.serialize_ec2_query(
            value["remove_subnet_ids"], pairs, f"{prefix}.RemoveSubnetIds"
        )
    if "options" in value:
        import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options

        aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayVpcAttachmentRequest:
    out: ModifyTransitGatewayVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    if el.find("AddSubnetIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        out["add_subnet_ids"] = (
            aws_sdk_ec2.types.transit_gateway_subnet_id_list.deserialize_ec2_query(
                el, "AddSubnetIds"
            )
        )
    if el.find("RemoveSubnetIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        out["remove_subnet_ids"] = (
            aws_sdk_ec2.types.transit_gateway_subnet_id_list.deserialize_ec2_query(
                el, "RemoveSubnetIds"
            )
        )
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options

        out["options"] = (
            aws_sdk_ec2.types.modify_transit_gateway_vpc_attachment_request_options.deserialize_ec2_query(
                child_options
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
