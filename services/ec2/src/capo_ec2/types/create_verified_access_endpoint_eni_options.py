"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointEniOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_verified_access_endpoint_port_range_list
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.verified_access_endpoint_port_number
    import capo_ec2.types.verified_access_endpoint_protocol


class CreateVerifiedAccessEndpointEniOptions(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    protocol: NotRequired[
        "capo_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "capo_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    port_ranges: NotRequired[
        "capo_ec2.types.create_verified_access_endpoint_port_range_list.CreateVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointEniOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "protocol" in value:
        import capo_ec2.types.verified_access_endpoint_protocol

        capo_ec2.types.verified_access_endpoint_protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{key_prefix}Protocol"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "port_ranges" in value:
        import capo_ec2.types.create_verified_access_endpoint_port_range_list

        capo_ec2.types.create_verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{key_prefix}PortRange"
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessEndpointEniOptions:
    out: CreateVerifiedAccessEndpointEniOptions = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.verified_access_endpoint_protocol

        out["protocol"] = (
            capo_ec2.types.verified_access_endpoint_protocol.deserialize_ec2_query(
                child_protocol
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    if el.find("PortRange") is not None:
        import capo_ec2.types.create_verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            capo_ec2.types.create_verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRange"
            )
        )
    return out
