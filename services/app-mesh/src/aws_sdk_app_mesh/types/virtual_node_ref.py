"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeRef``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_app_mesh.types.account_id
    import aws_sdk_app_mesh.types.arn
    import aws_sdk_app_mesh.types.resource_name


class VirtualNodeRef(TypedDict, closed=True):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual node resides in.</p>"""
    virtual_node_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual node.</p>"""
    mesh_owner: "aws_sdk_app_mesh.types.account_id.AccountId"
    r"""<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""
    resource_owner: "aws_sdk_app_mesh.types.account_id.AccountId"
    r"""<p>The Amazon Web Services IAM account ID of the resource owner. If the account ID is not your own, then it's the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""
    arn: "aws_sdk_app_mesh.types.arn.Arn"
    """<p>The full Amazon Resource Name (ARN) for the virtual node.</p>"""
    version: "int"
    """<p>The version of the resource. Resources are created at version 1, and this version is incremented each time that they're updated.</p>"""
    created_at: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds for when the resource was created.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds for when the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeRef) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualNodeName"] = value["virtual_node_name"]
    out["meshOwner"] = value["mesh_owner"]
    out["resourceOwner"] = value["resource_owner"]
    out["arn"] = value["arn"]
    out["version"] = value["version"]
    import aws_sdk_app_mesh.types._prelude.timestamp

    out["createdAt"] = aws_sdk_app_mesh.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_app_mesh.types._prelude.timestamp

    out["lastUpdatedAt"] = aws_sdk_app_mesh.types._prelude.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> VirtualNodeRef:
    out: VirtualNodeRef = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("VirtualNodeRef.mesh_name required")
    if "virtualNodeName" in data:
        out["virtual_node_name"] = data["virtualNodeName"]
    else:
        raise DeserializationError("VirtualNodeRef.virtual_node_name required")
    if "meshOwner" in data:
        out["mesh_owner"] = data["meshOwner"]
    else:
        raise DeserializationError("VirtualNodeRef.mesh_owner required")
    if "resourceOwner" in data:
        out["resource_owner"] = data["resourceOwner"]
    else:
        raise DeserializationError("VirtualNodeRef.resource_owner required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("VirtualNodeRef.arn required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("VirtualNodeRef.version required")
    if "createdAt" in data:
        import aws_sdk_app_mesh.types._prelude.timestamp

        out["created_at"] = aws_sdk_app_mesh.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("VirtualNodeRef.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_app_mesh.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_app_mesh.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("VirtualNodeRef.last_updated_at required")
    return out
