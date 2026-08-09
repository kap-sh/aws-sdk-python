"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.create_transit_gateway_connect_request_options
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_gateway_attachment_id


class CreateTransitGatewayConnectRequest(TypedDict, closed=True):
    transport_transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment. You can specify a VPC attachment or Amazon Web Services Direct Connect attachment.</p>"""
    options: NotRequired[
        "capo_ec2.types.create_transit_gateway_connect_request_options.CreateTransitGatewayConnectRequestOptions"
    ]
    """<p>The Connect attachment options.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Connect attachment.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayConnectRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transport_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransportTransitGatewayAttachmentId",
                str(value["transport_transit_gateway_attachment_id"]),
            )
        )
    if "options" in value:
        import capo_ec2.types.create_transit_gateway_connect_request_options

        capo_ec2.types.create_transit_gateway_connect_request_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayConnectRequest:
    out: CreateTransitGatewayConnectRequest = {}  # type: ignore[typeddict-item]
    child_transport_transit_gateway_attachment_id = el.find(
        "TransportTransitGatewayAttachmentId"
    )
    if child_transport_transit_gateway_attachment_id is not None:
        out["transport_transit_gateway_attachment_id"] = str(
            child_transport_transit_gateway_attachment_id.text or ""
        )
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.create_transit_gateway_connect_request_options

        out["options"] = (
            capo_ec2.types.create_transit_gateway_connect_request_options.deserialize_ec2_query(
                child_options
            )
        )
    child_tag_specifications = el.find("TagSpecification")
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
