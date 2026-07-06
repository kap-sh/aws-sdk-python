"""Generated from Smithy shape ``com.amazonaws.appmesh#ListMeshesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.mesh_list


class ListMeshesOutput(TypedDict, closed=True):
    meshes: "aws_sdk_app_mesh.types.mesh_list.MeshList"
    """<p>The list of existing service meshes.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListMeshes</code> request. When the results of a <code>ListMeshes</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMeshesOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.mesh_list

    out["meshes"] = aws_sdk_app_mesh.types.mesh_list.serialize_json(value["meshes"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMeshesOutput:
    out: ListMeshesOutput = {}  # type: ignore[typeddict-item]
    if "meshes" in data:
        import aws_sdk_app_mesh.types.mesh_list

        out["meshes"] = aws_sdk_app_mesh.types.mesh_list.deserialize_json(
            data["meshes"]
        )
    else:
        raise DeserializationError("ListMeshesOutput.meshes required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
