"""Generated from Smithy shape ``com.amazonaws.medialive#NodeInterfaceMappingCreateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.network_interface_mode


class NodeInterfaceMappingCreateRequest(TypedDict, closed=True):
    logical_interface_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specify one of the logicalInterfaceNames that you created in the Cluster that this node belongs to. For example, my-Inputs-Interface."""
    network_interface_mode: NotRequired[
        "aws_sdk_medialive.types.network_interface_mode.NetworkInterfaceMode"
    ]
    """The style of the network -- NAT or BRIDGE."""
    physical_interface_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specify the physical name that corresponds to the logicalInterfaceName that you specified in this interface mapping. For example, Eth1 or ENO1234EXAMPLE."""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInterfaceMappingCreateRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> NodeInterfaceMappingCreateRequest:
    out: NodeInterfaceMappingCreateRequest = {}  # type: ignore[typeddict-item]
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
    return out
