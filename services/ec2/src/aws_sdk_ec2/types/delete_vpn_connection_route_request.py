"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpnConnectionRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id


class DeleteVpnConnectionRouteRequest(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block associated with the local subnet of the customer network.</p>"""
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the VPN connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVpnConnectionRouteRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))


def deserialize_ec2_query(el: Element) -> DeleteVpnConnectionRouteRequest:
    out: DeleteVpnConnectionRouteRequest = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    return out
