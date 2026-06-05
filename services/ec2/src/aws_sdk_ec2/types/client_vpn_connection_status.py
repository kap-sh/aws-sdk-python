"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_status_code
    import aws_sdk_ec2.types.string


class ClientVpnConnectionStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status_code.ClientVpnConnectionStatusCode"
    ]
    """<p>The state of the client connection.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the client connection, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnConnectionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import aws_sdk_ec2.types.client_vpn_connection_status_code

        aws_sdk_ec2.types.client_vpn_connection_status_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> ClientVpnConnectionStatus:
    out: ClientVpnConnectionStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_ec2.types.client_vpn_connection_status_code

        out["code"] = (
            aws_sdk_ec2.types.client_vpn_connection_status_code.deserialize_ec2_query(
                child_code
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
