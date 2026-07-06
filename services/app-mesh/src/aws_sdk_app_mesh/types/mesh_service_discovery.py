"""Generated from Smithy shape ``com.amazonaws.appmesh#MeshServiceDiscovery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.ip_preference


class MeshServiceDiscovery(TypedDict, closed=True):
    ip_preference: NotRequired["aws_sdk_app_mesh.types.ip_preference.IpPreference"]
    """<p>The IP version to use to control traffic within the mesh.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeshServiceDiscovery) -> dict:
    out: dict = {}
    if "ip_preference" in value:
        out["ipPreference"] = value["ip_preference"]
    return out


def deserialize_json(data: dict) -> MeshServiceDiscovery:
    out: MeshServiceDiscovery = {}  # type: ignore[typeddict-item]
    if "ipPreference" in data:
        out["ip_preference"] = data["ipPreference"]
    return out
