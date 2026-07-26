"""Generated from Smithy shape ``com.amazonaws.appmesh#MeshStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.mesh_status_code


class MeshStatus(TypedDict, closed=True):
    status: NotRequired["capo_app_mesh.types.mesh_status_code.MeshStatusCode"]
    """<p>The current mesh status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeshStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> MeshStatus:
    out: MeshStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
