"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateMeshInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.mesh_spec
    import aws_sdk_app_mesh.types.resource_name
    import aws_sdk_app_mesh.types.tag_list


class CreateMeshInput(TypedDict):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name to use for the service mesh.</p>"""
    spec: NotRequired["aws_sdk_app_mesh.types.mesh_spec.MeshSpec"]
    """<p>The service mesh specification to apply.</p>"""
    tags: NotRequired["aws_sdk_app_mesh.types.tag_list.TagList"]
    """<p>Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeshInput) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    if "spec" in value:
        import aws_sdk_app_mesh.types.mesh_spec

        out["spec"] = aws_sdk_app_mesh.types.mesh_spec.serialize_json(value["spec"])
    if "tags" in value:
        import aws_sdk_app_mesh.types.tag_list

        out["tags"] = aws_sdk_app_mesh.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateMeshInput:
    out: CreateMeshInput = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("CreateMeshInput.mesh_name required")
    if "spec" in data:
        import aws_sdk_app_mesh.types.mesh_spec

        out["spec"] = aws_sdk_app_mesh.types.mesh_spec.deserialize_json(data["spec"])
    if "tags" in data:
        import aws_sdk_app_mesh.types.tag_list

        out["tags"] = aws_sdk_app_mesh.types.tag_list.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
