"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_status
    import aws_sdk_ec2.types.string


class TerminateConnectionStatus(TypedDict):
    connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the client connection.</p>"""
    previous_status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>The state of the client connection.</p>"""
    current_status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>A message about the status of the client connection, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TerminateConnectionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "connection_id" in value:
        pairs.append((f"{prefix}.ConnectionId", str(value["connection_id"])))
    if "previous_status" in value:
        import aws_sdk_ec2.types.client_vpn_connection_status

        aws_sdk_ec2.types.client_vpn_connection_status.serialize_ec2_query(
            value["previous_status"], pairs, f"{prefix}.PreviousStatus"
        )
    if "current_status" in value:
        import aws_sdk_ec2.types.client_vpn_connection_status

        aws_sdk_ec2.types.client_vpn_connection_status.serialize_ec2_query(
            value["current_status"], pairs, f"{prefix}.CurrentStatus"
        )


def deserialize_ec2_query(el: Element) -> TerminateConnectionStatus:
    out: TerminateConnectionStatus = {}  # type: ignore[typeddict-item]
    child_connection_id = el.find("ConnectionId")
    if child_connection_id is not None:
        out["connection_id"] = str(child_connection_id.text or "")
    child_previous_status = el.find("PreviousStatus")
    if child_previous_status is not None:
        import aws_sdk_ec2.types.client_vpn_connection_status

        out["previous_status"] = (
            aws_sdk_ec2.types.client_vpn_connection_status.deserialize_ec2_query(
                child_previous_status
            )
        )
    child_current_status = el.find("CurrentStatus")
    if child_current_status is not None:
        import aws_sdk_ec2.types.client_vpn_connection_status

        out["current_status"] = (
            aws_sdk_ec2.types.client_vpn_connection_status.deserialize_ec2_query(
                child_current_status
            )
        )
    return out
