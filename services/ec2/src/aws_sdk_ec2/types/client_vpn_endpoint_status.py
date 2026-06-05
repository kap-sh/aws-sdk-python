"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnEndpointStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_status_code
    import aws_sdk_ec2.types.string


class ClientVpnEndpointStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_status_code.ClientVpnEndpointStatusCode"
    ]
    """<p>The state of the Client VPN endpoint. Possible states include:</p> <ul> <li> <p> <code>pending-associate</code> - The Client VPN endpoint has been created but no target networks have been associated. The Client VPN endpoint cannot accept connections.</p> </li> <li> <p> <code>available</code> - The Client VPN endpoint has been created and a target network has been associated. The Client VPN endpoint can accept connections.</p> </li> <li> <p> <code>deleting</code> - The Client VPN endpoint is being deleted. The Client VPN endpoint cannot accept connections.</p> </li> <li> <p> <code>deleted</code> - The Client VPN endpoint has been deleted. The Client VPN endpoint cannot accept connections.</p> </li> <li> <p> <code>pending</code> - The Client VPN endpoint has been created with a Transit Gateway configuration and is waiting for the Transit Gateway attachment to be accepted. The Client VPN endpoint cannot accept connections.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the Client VPN endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnEndpointStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import aws_sdk_ec2.types.client_vpn_endpoint_status_code

        aws_sdk_ec2.types.client_vpn_endpoint_status_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> ClientVpnEndpointStatus:
    out: ClientVpnEndpointStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_ec2.types.client_vpn_endpoint_status_code

        out["code"] = (
            aws_sdk_ec2.types.client_vpn_endpoint_status_code.deserialize_ec2_query(
                child_code
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
