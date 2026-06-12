"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteVirtualRouterOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_router_data

class DeleteVirtualRouterOutput(TypedDict):
    virtual_router: "aws_sdk_app_mesh.types.virtual_router_data.VirtualRouterData"
    """<p>The virtual router that was deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteVirtualRouterOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_router_data
    out["virtualRouter"] = aws_sdk_app_mesh.types.virtual_router_data.serialize_json(value["virtual_router"])
    return out


def deserialize_json(data: dict) -> DeleteVirtualRouterOutput:
    out: DeleteVirtualRouterOutput = {}  # type: ignore[typeddict-item]
    if "virtualRouter" in data:
        import aws_sdk_app_mesh.types.virtual_router_data
        out["virtual_router"] = aws_sdk_app_mesh.types.virtual_router_data.deserialize_json(data["virtualRouter"])
    else:
        raise DeserializationError("DeleteVirtualRouterOutput.virtual_router required")
    return out