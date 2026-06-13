"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterServiceProvider``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_name


class VirtualRouterServiceProvider(TypedDict):
    virtual_router_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual router that is acting as a service provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterServiceProvider) -> dict:
    out: dict = {}
    out["virtualRouterName"] = value["virtual_router_name"]
    return out


def deserialize_json(data: dict) -> VirtualRouterServiceProvider:
    out: VirtualRouterServiceProvider = {}  # type: ignore[typeddict-item]
    if "virtualRouterName" in data:
        out["virtual_router_name"] = data["virtualRouterName"]
    else:
        raise DeserializationError(
            "VirtualRouterServiceProvider.virtual_router_name required"
        )
    return out
