"""Generated from Smithy shape ``com.amazonaws.medialive#NodeInterfaceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.network_interface_mode


class NodeInterfaceMapping(TypedDict, closed=True):
    logical_interface_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A uniform logical interface name to address in a MediaLive channel configuration."""
    network_interface_mode: NotRequired[
        "aws_sdk_medialive.types.network_interface_mode.NetworkInterfaceMode"
    ]
    physical_interface_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the physical interface on the hardware that will be running Elemental anywhere."""
    physical_interface_ip_addresses: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The IP addresses associated with the physical interface on the node hardware."""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInterfaceMapping) -> dict:
    out: dict = {}
    if "logical_interface_name" in value:
        out["logicalInterfaceName"] = value["logical_interface_name"]
    if "network_interface_mode" in value:
        import aws_sdk_medialive.types.network_interface_mode

        out["networkInterfaceMode"] = (
            aws_sdk_medialive.types.network_interface_mode.serialize_json(
                value["network_interface_mode"]
            )
        )
    if "physical_interface_name" in value:
        out["physicalInterfaceName"] = value["physical_interface_name"]
    if "physical_interface_ip_addresses" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["physicalInterfaceIpAddresses"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["physical_interface_ip_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeInterfaceMapping:
    out: NodeInterfaceMapping = {}  # type: ignore[typeddict-item]
    if "logicalInterfaceName" in data:
        out["logical_interface_name"] = data["logicalInterfaceName"]
    if "networkInterfaceMode" in data:
        import aws_sdk_medialive.types.network_interface_mode

        out["network_interface_mode"] = (
            aws_sdk_medialive.types.network_interface_mode.deserialize_json(
                data["networkInterfaceMode"]
            )
        )
    if "physicalInterfaceName" in data:
        out["physical_interface_name"] = data["physicalInterfaceName"]
    if "physicalInterfaceIpAddresses" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["physical_interface_ip_addresses"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["physicalInterfaceIpAddresses"]
            )
        )
    return out
