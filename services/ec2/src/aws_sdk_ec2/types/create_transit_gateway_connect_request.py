"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_transit_gateway_connect_request_options
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_attachment_id


class CreateTransitGatewayConnectRequest(TypedDict):
    transport_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment. You can specify a VPC attachment or Amazon Web Services Direct Connect attachment.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.create_transit_gateway_connect_request_options.CreateTransitGatewayConnectRequestOptions"
    ]
    """<p>The Connect attachment options.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Connect attachment.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayConnectRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transport_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransportTransitGatewayAttachmentId",
                str(value["transport_transit_gateway_attachment_id"]),
            )
        )
    if "options" in value:
        import aws_sdk_ec2.types.create_transit_gateway_connect_request_options

        aws_sdk_ec2.types.create_transit_gateway_connect_request_options.serialize_ec2_query(
            value["options"], pairs, f"{prefix}.Options"
        )
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


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
        import aws_sdk_ec2.types.create_transit_gateway_connect_request_options

        out["options"] = (
            aws_sdk_ec2.types.create_transit_gateway_connect_request_options.deserialize_ec2_query(
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
