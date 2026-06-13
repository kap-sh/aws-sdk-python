"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_router_status_code


class VirtualRouterStatus(TypedDict):
    status: "aws_sdk_app_mesh.types.virtual_router_status_code.VirtualRouterStatusCode"
    """<p>The current status of the virtual router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualRouterStatus:
    out: VirtualRouterStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("VirtualRouterStatus.status required")
    return out
