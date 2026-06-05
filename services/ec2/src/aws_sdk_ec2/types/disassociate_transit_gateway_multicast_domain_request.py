"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTransitGatewayMulticastDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_id
    import aws_sdk_ec2.types.transit_gateway_subnet_id_list


class DisassociateTransitGatewayMulticastDomainRequest(TypedDict):
    transit_gateway_multicast_domain_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
    ]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the attachment.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_subnet_id_list.TransitGatewaySubnetIdList"
    ]
    """<p>The IDs of the subnets;</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateTransitGatewayMulticastDomainRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        aws_sdk_ec2.types.transit_gateway_subnet_id_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{prefix}.SubnetIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> DisassociateTransitGatewayMulticastDomainRequest:
    out: DisassociateTransitGatewayMulticastDomainRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain_id = el.find(
        "TransitGatewayMulticastDomainId"
    )
    if child_transit_gateway_multicast_domain_id is not None:
        out["transit_gateway_multicast_domain_id"] = str(
            child_transit_gateway_multicast_domain_id.text or ""
        )
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    if el.find("SubnetIds") is not None:
        import aws_sdk_ec2.types.transit_gateway_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_ec2.types.transit_gateway_subnet_id_list.deserialize_ec2_query(
                el, "SubnetIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
