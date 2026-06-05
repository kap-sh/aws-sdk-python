"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointEniOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.verified_access_endpoint_port_number
    import aws_sdk_ec2.types.verified_access_endpoint_protocol


class CreateVerifiedAccessEndpointEniOptions(TypedDict):
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.CreateVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointEniOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "protocol" in value:
        import aws_sdk_ec2.types.verified_access_endpoint_protocol

        aws_sdk_ec2.types.verified_access_endpoint_protocol.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "port" in value:
        pairs.append((f"{prefix}.Port", str(value["port"])))
    if "port_ranges" in value:
        import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list

        aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{prefix}.PortRanges"
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessEndpointEniOptions:
    out: CreateVerifiedAccessEndpointEniOptions = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_ec2.types.verified_access_endpoint_protocol

        out["protocol"] = (
            aws_sdk_ec2.types.verified_access_endpoint_protocol.deserialize_ec2_query(
                child_protocol
            )
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    if el.find("PortRanges") is not None:
        import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRanges"
            )
        )
    return out
