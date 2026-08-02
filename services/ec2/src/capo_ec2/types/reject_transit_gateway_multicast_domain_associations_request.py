"""Generated from Smithy shape ``com.amazonaws.ec2#RejectTransitGatewayMulticastDomainAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_multicast_domain_id
    import capo_ec2.types.value_string_list


class RejectTransitGatewayMulticastDomainAssociationsRequest(TypedDict, closed=True):
    transit_gateway_multicast_domain_id: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
    ]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment.</p>"""
    subnet_ids: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the subnets to associate with the transit gateway multicast domain.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RejectTransitGatewayMulticastDomainAssociationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_multicast_domain_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayMulticastDomainId",
                str(value["transit_gateway_multicast_domain_id"]),
            )
        )
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "subnet_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["subnet_ids"], pairs, f"{key_prefix}SubnetIds"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> RejectTransitGatewayMulticastDomainAssociationsRequest:
    out: RejectTransitGatewayMulticastDomainAssociationsRequest = {}  # type: ignore[typeddict-item]
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
        import capo_ec2.types.value_string_list

        out["subnet_ids"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SubnetIds"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
