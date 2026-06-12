"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterNetworkSettingsUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_interface_mapping_update_request
    import aws_sdk_medialive.types.__string


class ClusterNetworkSettingsUpdateRequest(TypedDict):
    default_route: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Include this parameter only if you want to change the default route for the Cluster. Specify one network interface as the default route for traffic to and from the node. MediaLive Anywhere uses this default when the destination for the traffic isn't covered by the route table for any of the networks. Specify the value of the appropriate logicalInterfaceName parameter that you create in the interfaceMappings."""
    interface_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_interface_mapping_update_request.__listOfInterfaceMappingUpdateRequest"
    ]
    """An array of interfaceMapping objects for this Cluster. Include this parameter only if you want to change the interface mappings for the Cluster. Typically, you change the interface mappings only to fix an error you made when creating the mapping. In an update request, make sure that you enter the entire set of mappings again, not just the mappings that you want to add or change. You define this mapping so that the mapping can be used by all the Nodes. Each mapping logically connects one interface on the nodes with one Network. Each mapping consists of a pair of parameters. The logicalInterfaceName parameter creates a logical name for the Node interface that handles a specific type of traffic. For example, my-Inputs-Interface. The networkID parameter refers to the ID of the network. When you create the Nodes in this Cluster, you will associate the logicalInterfaceName with the appropriate physical interface."""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterNetworkSettingsUpdateRequest) -> dict:
    out: dict = {}
    if "default_route" in value:
        out["defaultRoute"] = value["default_route"]
    if "interface_mappings" in value:
        import aws_sdk_medialive.types.__list_of_interface_mapping_update_request

        out["interfaceMappings"] = (
            aws_sdk_medialive.types.__list_of_interface_mapping_update_request.serialize_json(
                value["interface_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterNetworkSettingsUpdateRequest:
    out: ClusterNetworkSettingsUpdateRequest = {}  # type: ignore[typeddict-item]
    if "defaultRoute" in data:
        out["default_route"] = data["defaultRoute"]
    if "interfaceMappings" in data:
        import aws_sdk_medialive.types.__list_of_interface_mapping_update_request

        out["interface_mappings"] = (
            aws_sdk_medialive.types.__list_of_interface_mapping_update_request.deserialize_json(
                data["interfaceMappings"]
            )
        )
    return out
