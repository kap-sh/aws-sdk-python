"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateConnectionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_connection_status
    import capo_ec2.types.string


class TerminateConnectionStatus(TypedDict, closed=True):
    connection_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the client connection.</p>"""
    previous_status: NotRequired[
        "capo_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>The state of the client connection.</p>"""
    current_status: NotRequired[
        "capo_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>A message about the status of the client connection, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateConnectionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "connection_id" in value:
        pairs.append((f"{key_prefix}ConnectionId", str(value["connection_id"])))
    if "previous_status" in value:
        import capo_ec2.types.client_vpn_connection_status

        capo_ec2.types.client_vpn_connection_status.serialize_ec2_query(
            value["previous_status"], pairs, f"{key_prefix}PreviousStatus"
        )
    if "current_status" in value:
        import capo_ec2.types.client_vpn_connection_status

        capo_ec2.types.client_vpn_connection_status.serialize_ec2_query(
            value["current_status"], pairs, f"{key_prefix}CurrentStatus"
        )


def deserialize_ec2_query(el: Element) -> TerminateConnectionStatus:
    out: TerminateConnectionStatus = {}  # type: ignore[typeddict-item]
    child_connection_id = el.find("ConnectionId")
    if child_connection_id is not None:
        out["connection_id"] = str(child_connection_id.text or "")
    child_previous_status = el.find("PreviousStatus")
    if child_previous_status is not None:
        import capo_ec2.types.client_vpn_connection_status

        out["previous_status"] = (
            capo_ec2.types.client_vpn_connection_status.deserialize_ec2_query(
                child_previous_status
            )
        )
    child_current_status = el.find("CurrentStatus")
    if child_current_status is not None:
        import capo_ec2.types.client_vpn_connection_status

        out["current_status"] = (
            capo_ec2.types.client_vpn_connection_status.deserialize_ec2_query(
                child_current_status
            )
        )
    return out
