"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeServiceProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_name


class VirtualNodeServiceProvider(TypedDict, closed=True):
    virtual_node_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual node that is acting as a service provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeServiceProvider) -> dict:
    out: dict = {}
    out["virtualNodeName"] = value["virtual_node_name"]
    return out


def deserialize_json(data: dict) -> VirtualNodeServiceProvider:
    out: VirtualNodeServiceProvider = {}  # type: ignore[typeddict-item]
    if "virtualNodeName" in data:
        out["virtual_node_name"] = data["virtualNodeName"]
    else:
        raise DeserializationError(
            "VirtualNodeServiceProvider.virtual_node_name required"
        )
    return out
