"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayRef``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_app_mesh.types.account_id
    import aws_sdk_app_mesh.types.arn
    import aws_sdk_app_mesh.types.resource_name


class VirtualGatewayRef(TypedDict):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the resource resides in.</p>"""
    virtual_gateway_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the resource.</p>"""
    mesh_owner: "aws_sdk_app_mesh.types.account_id.AccountId"
    r"""<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""
    resource_owner: "aws_sdk_app_mesh.types.account_id.AccountId"
    r"""<p>The Amazon Web Services IAM account ID of the resource owner. If the account ID is not your own, then it's the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""
    arn: "aws_sdk_app_mesh.types.arn.Arn"
    """<p>The full Amazon Resource Name (ARN) for the resource.</p>"""
    version: "int"
    """<p>The version of the resource. Resources are created at version 1, and this version is incremented each time that they're updated.</p>"""
    created_at: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds for when the resource was created.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>The Unix epoch timestamp in seconds for when the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayRef) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualGatewayName"] = value["virtual_gateway_name"]
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


def deserialize_json(data: dict) -> VirtualGatewayRef:
    out: VirtualGatewayRef = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("VirtualGatewayRef.mesh_name required")
    if "virtualGatewayName" in data:
        out["virtual_gateway_name"] = data["virtualGatewayName"]
    else:
        raise DeserializationError("VirtualGatewayRef.virtual_gateway_name required")
    if "meshOwner" in data:
        out["mesh_owner"] = data["meshOwner"]
    else:
        raise DeserializationError("VirtualGatewayRef.mesh_owner required")
    if "resourceOwner" in data:
        out["resource_owner"] = data["resourceOwner"]
    else:
        raise DeserializationError("VirtualGatewayRef.resource_owner required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("VirtualGatewayRef.arn required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("VirtualGatewayRef.version required")
    if "createdAt" in data:
        import aws_sdk_app_mesh.types._prelude.timestamp

        out["created_at"] = aws_sdk_app_mesh.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("VirtualGatewayRef.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_app_mesh.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_app_mesh.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("VirtualGatewayRef.last_updated_at required")
    return out
