"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerPropertyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.listener_property_type
    import capo_network_firewall.types.nat_gateway_port


class ListenerPropertyRequest(TypedDict, closed=True):
    port: "capo_network_firewall.types.nat_gateway_port.NatGatewayPort"
    """<p>Port for processing traffic.</p>"""
    type: "capo_network_firewall.types.listener_property_type.ListenerPropertyType"
    """<p>Selection of HTTP or HTTPS traffic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerPropertyRequest) -> dict:
    out: dict = {}
    out["Port"] = value["port"]
    import capo_network_firewall.types.listener_property_type

    out["Type"] = (
        capo_network_firewall.types.listener_property_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListenerPropertyRequest:
    out: ListenerPropertyRequest = {}  # type: ignore[typeddict-item]
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("ListenerPropertyRequest.port required")
    if "Type" in data:
        import capo_network_firewall.types.listener_property_type

        out["type"] = (
            capo_network_firewall.types.listener_property_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ListenerPropertyRequest.type required")
    return out
