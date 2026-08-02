"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateClientVpnConnectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.terminate_connection_status_set


class TerminateClientVpnConnectionsResult(TypedDict, closed=True):
    client_vpn_endpoint_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    username: NotRequired["capo_ec2.types.string.String"]
    """<p>The user who established the terminated client connections.</p>"""
    connection_statuses: NotRequired[
        "capo_ec2.types.terminate_connection_status_set.TerminateConnectionStatusSet"
    ]
    """<p>The current state of the client connections.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateClientVpnConnectionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_vpn_endpoint_id" in value:
        pairs.append(
            (f"{key_prefix}ClientVpnEndpointId", str(value["client_vpn_endpoint_id"]))
        )
    if "username" in value:
        pairs.append((f"{key_prefix}Username", str(value["username"])))
    if "connection_statuses" in value:
        import capo_ec2.types.terminate_connection_status_set

        capo_ec2.types.terminate_connection_status_set.serialize_ec2_query(
            value["connection_statuses"], pairs, f"{key_prefix}ConnectionStatuses"
        )


def deserialize_ec2_query(el: Element) -> TerminateClientVpnConnectionsResult:
    out: TerminateClientVpnConnectionsResult = {}  # type: ignore[typeddict-item]
    child_client_vpn_endpoint_id = el.find("ClientVpnEndpointId")
    if child_client_vpn_endpoint_id is not None:
        out["client_vpn_endpoint_id"] = str(child_client_vpn_endpoint_id.text or "")
    child_username = el.find("Username")
    if child_username is not None:
        out["username"] = str(child_username.text or "")
    if el.find("ConnectionStatuses") is not None:
        import capo_ec2.types.terminate_connection_status_set

        out["connection_statuses"] = (
            capo_ec2.types.terminate_connection_status_set.deserialize_ec2_query(
                el, "ConnectionStatuses"
            )
        )
    return out
