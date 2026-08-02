"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateClientVpnConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_vpn_endpoint_id
    import capo_ec2.types.string


class TerminateClientVpnConnectionsRequest(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired[
        "capo_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint to which the client is connected.</p>"""
    connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the client connection to be terminated.</p>"""
    username: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the user who initiated the connection. Use this option to terminate all active connections for the specified user. This option can only be used if the user has established up to five connections.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateClientVpnConnectionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "connection_id" in value:
        pairs.append((f"{key_prefix}ConnectionId", str(value["connection_id"])))
    if "username" in value:
        pairs.append((f"{key_prefix}Username", str(value["username"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> TerminateClientVpnConnectionsRequest:
    out: TerminateClientVpnConnectionsRequest = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_connection_id = el.find("ConnectionId")
    if child_connection_id is not None:
        out["connection_id"] = str(child_connection_id.text or "")
    child_username = el.find("Username")
    if child_username is not None:
        out["username"] = str(child_username.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
