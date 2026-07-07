"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.listener_property_type
    import aws_sdk_network_firewall.types.nat_gateway_port


class ListenerProperty(TypedDict, closed=True):
    port: NotRequired["aws_sdk_network_firewall.types.nat_gateway_port.NatGatewayPort"]
    """<p>Port for processing traffic.</p>"""
    type: NotRequired[
        "aws_sdk_network_firewall.types.listener_property_type.ListenerPropertyType"
    ]
    """<p>Selection of HTTP or HTTPS traffic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerProperty) -> dict:
    out: dict = {}
    if "port" in value:
        out["Port"] = value["port"]
    if "type" in value:
        import aws_sdk_network_firewall.types.listener_property_type

        out["Type"] = (
            aws_sdk_network_firewall.types.listener_property_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListenerProperty:
    out: ListenerProperty = {}  # type: ignore[typeddict-item]
    if "Port" in data:
        out["port"] = data["Port"]
    if "Type" in data:
        import aws_sdk_network_firewall.types.listener_property_type

        out["type"] = (
            aws_sdk_network_firewall.types.listener_property_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    return out
