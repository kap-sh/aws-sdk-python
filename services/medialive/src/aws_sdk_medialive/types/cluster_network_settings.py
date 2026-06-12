"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterNetworkSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_interface_mapping
    import aws_sdk_medialive.types.__string


class ClusterNetworkSettings(TypedDict):
    default_route: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The network interface that is the default route for traffic to and from the node. MediaLive Anywhere uses this default when the destination for the traffic isn't covered by the route table for any of the networks. Specify the value of the appropriate logicalInterfaceName parameter that you create in the interfaceMappings."""
    interface_mappings: NotRequired[
        "aws_sdk_medialive.types.__list_of_interface_mapping.__listOfInterfaceMapping"
    ]
    """An array of interfaceMapping objects for this Cluster. Each mapping logically connects one interface on the nodes with one Network. You need only one mapping for each interface because all the Nodes share the mapping."""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterNetworkSettings) -> dict:
    out: dict = {}
    if "default_route" in value:
        out["defaultRoute"] = value["default_route"]
    if "interface_mappings" in value:
        import aws_sdk_medialive.types.__list_of_interface_mapping

        out["interfaceMappings"] = (
            aws_sdk_medialive.types.__list_of_interface_mapping.serialize_json(
                value["interface_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterNetworkSettings:
    out: ClusterNetworkSettings = {}  # type: ignore[typeddict-item]
    if "defaultRoute" in data:
        out["default_route"] = data["defaultRoute"]
    if "interfaceMappings" in data:
        import aws_sdk_medialive.types.__list_of_interface_mapping

        out["interface_mappings"] = (
            aws_sdk_medialive.types.__list_of_interface_mapping.deserialize_json(
                data["interfaceMappings"]
            )
        )
    return out
