"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_node_status_code


class VirtualNodeStatus(TypedDict):
    status: "aws_sdk_app_mesh.types.virtual_node_status_code.VirtualNodeStatusCode"
    """<p>The current status of the virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualNodeStatus:
    out: VirtualNodeStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("VirtualNodeStatus.status required")
    return out
