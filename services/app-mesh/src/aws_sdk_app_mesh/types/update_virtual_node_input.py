"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateVirtualNodeInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.account_id
    import aws_sdk_app_mesh.types.resource_name
    import aws_sdk_app_mesh.types.virtual_node_spec


class UpdateVirtualNodeInput(TypedDict):
    virtual_node_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual node to update.</p>"""
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual node resides in.</p>"""
    spec: "aws_sdk_app_mesh.types.virtual_node_spec.VirtualNodeSpec"
    """<p>The new virtual node specification to apply. This overwrites the existing data.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""
    mesh_owner: NotRequired["aws_sdk_app_mesh.types.account_id.AccountId"]
    """<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualNodeInput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_node_spec

    out["spec"] = aws_sdk_app_mesh.types.virtual_node_spec.serialize_json(value["spec"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateVirtualNodeInput:
    out: UpdateVirtualNodeInput = {}  # type: ignore[typeddict-item]
    if "spec" in data:
        import aws_sdk_app_mesh.types.virtual_node_spec

        out["spec"] = aws_sdk_app_mesh.types.virtual_node_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("UpdateVirtualNodeInput.spec required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
