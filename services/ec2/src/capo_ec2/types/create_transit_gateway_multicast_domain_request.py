"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMulticastDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.create_transit_gateway_multicast_domain_request_options
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_gateway_id


class CreateTransitGatewayMulticastDomainRequest(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    options: NotRequired[
        "capo_ec2.types.create_transit_gateway_multicast_domain_request_options.CreateTransitGatewayMulticastDomainRequestOptions"
    ]
    """<p>The options for the transit gateway multicast domain.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags for the transit gateway multicast domain.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayMulticastDomainRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "options" in value:
        import capo_ec2.types.create_transit_gateway_multicast_domain_request_options

        capo_ec2.types.create_transit_gateway_multicast_domain_request_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayMulticastDomainRequest:
    out: CreateTransitGatewayMulticastDomainRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.create_transit_gateway_multicast_domain_request_options

        out["options"] = (
            capo_ec2.types.create_transit_gateway_multicast_domain_request_options.deserialize_ec2_query(
                child_options
            )
        )
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
