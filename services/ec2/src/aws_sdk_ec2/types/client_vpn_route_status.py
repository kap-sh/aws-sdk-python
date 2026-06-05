"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnRouteStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_status_code
    import aws_sdk_ec2.types.string


class ClientVpnRouteStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_route_status_code.ClientVpnRouteStatusCode"
    ]
    """<p>The state of the Client VPN endpoint route.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the Client VPN endpoint route, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnRouteStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import aws_sdk_ec2.types.client_vpn_route_status_code

        aws_sdk_ec2.types.client_vpn_route_status_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> ClientVpnRouteStatus:
    out: ClientVpnRouteStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_ec2.types.client_vpn_route_status_code

        out["code"] = (
            aws_sdk_ec2.types.client_vpn_route_status_code.deserialize_ec2_query(
                child_code
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
