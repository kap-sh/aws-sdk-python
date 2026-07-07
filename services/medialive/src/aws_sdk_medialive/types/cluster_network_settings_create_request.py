"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterNetworkSettingsCreateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_interface_mapping_create_request
    import aws_sdk_medialive.types.__string


class ClusterNetworkSettingsCreateRequest(TypedDict, closed=True):
    default_route: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specify one network interface as the default route for traffic to and from the Node. MediaLive Anywhere uses this default when the destination for the traffic isn't covered by the route table for any of the networks. Specify the value of the appropriate logicalInterfaceName parameter that you create in the interfaceMappings."""
    interface_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_interface_mapping_create_request.__listOfInterfaceMappingCreateRequest"
    ]
    """An array of interfaceMapping objects for this Cluster. You must create a mapping for node interfaces that you plan to use for encoding traffic. You typically don't create a mapping for the management interface. You define this mapping in the Cluster so that the mapping can be used by all the Nodes. Each mapping logically connects one interface on the nodes with one Network. Each mapping consists of a pair of parameters. The logicalInterfaceName parameter creates a logical name for the Node interface that handles a specific type of traffic. For example, my-Inputs-Interface. The networkID parameter refers to the ID of the network. When you create the Nodes in this Cluster, you will associate the logicalInterfaceName with the appropriate physical interface."""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterNetworkSettingsCreateRequest) -> dict:
    out: dict = {}
    if "default_route" in value:
        out["defaultRoute"] = value["default_route"]
    if "interface_mappings" in value:
        import aws_sdk_medialive.types.__list_of_interface_mapping_create_request

        out["interfaceMappings"] = (
            aws_sdk_medialive.types.__list_of_interface_mapping_create_request.serialize_json(
                value["interface_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterNetworkSettingsCreateRequest:
    out: ClusterNetworkSettingsCreateRequest = {}  # type: ignore[typeddict-item]
    if "defaultRoute" in data:
        out["default_route"] = data["defaultRoute"]
    if "interfaceMappings" in data:
        import aws_sdk_medialive.types.__list_of_interface_mapping_create_request

        out["interface_mappings"] = (
            aws_sdk_medialive.types.__list_of_interface_mapping_create_request.deserialize_json(
                data["interfaceMappings"]
            )
        )
    return out
