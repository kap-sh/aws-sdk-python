"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayClientVpnAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_status_type
    import aws_sdk_ec2.types.transit_gateway_id


class TransitGatewayClientVpnAttachment(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Transit Gateway attachment.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway.</p>"""
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    client_vpn_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Client VPN endpoint.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_status_type.TransitGatewayAttachmentStatusType"
    ]
    """<p>The state of the Transit Gateway attachment.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the Transit Gateway attachment was created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayClientVpnAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "client_vpn_owner_id" in value:
        pairs.append((f"{prefix}.ClientVpnOwnerId", str(value["client_vpn_owner_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_status_type

        aws_sdk_ec2.types.transit_gateway_attachment_status_type.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "creation_time" in value:
        pairs.append((f"{prefix}.CreationTime", str(value["creation_time"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayClientVpnAttachment:
    out: TransitGatewayClientVpnAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_client_vpn_owner_id = el.find("ClientVpnOwnerId")
    if child_client_vpn_owner_id is not None:
        out["client_vpn_owner_id"] = str(child_client_vpn_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_status_type

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_status_type.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        out["creation_time"] = str(child_creation_time.text or "")
    return out
