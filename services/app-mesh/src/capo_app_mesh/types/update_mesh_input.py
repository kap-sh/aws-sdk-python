"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateMeshInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.mesh_spec
    import capo_app_mesh.types.resource_name


class UpdateMeshInput(TypedDict, closed=True):
    mesh_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh to update.</p>"""
    spec: NotRequired["capo_app_mesh.types.mesh_spec.MeshSpec"]
    """<p>The service mesh specification to apply.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMeshInput) -> dict:
    out: dict = {}
    if "spec" in value:
        import capo_app_mesh.types.mesh_spec

        out["spec"] = capo_app_mesh.types.mesh_spec.serialize_json(value["spec"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateMeshInput:
    out: UpdateMeshInput = {}  # type: ignore[typeddict-item]
    if "spec" in data:
        import capo_app_mesh.types.mesh_spec

        out["spec"] = capo_app_mesh.types.mesh_spec.deserialize_json(data["spec"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
