"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnEndpointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_endpoint_status
    import capo_ec2.types.string


class CreateClientVpnEndpointResult(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    status: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_status.ClientVpnEndpointStatus"
    ]
    """<p>The current state of the Client VPN endpoint.</p>"""
    dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The DNS name to be used by clients when establishing their VPN session.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateClientVpnEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "status" in value:
        import capo_ec2.types.client_vpn_endpoint_status

        capo_ec2.types.client_vpn_endpoint_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "dns_name" in value:
        pairs.append((f"{prefix}.DnsName", str(value["dns_name"])))


def deserialize_ec2_query(el: Element) -> CreateClientVpnEndpointResult:
    out: CreateClientVpnEndpointResult = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.client_vpn_endpoint_status

        out["status"] = capo_ec2.types.client_vpn_endpoint_status.deserialize_ec2_query(
            child_status
        )
    child_dns_name = el.find("DnsName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    return out
