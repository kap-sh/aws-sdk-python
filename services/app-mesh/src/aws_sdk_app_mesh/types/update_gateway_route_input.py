"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateGatewayRouteInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.account_id
    import aws_sdk_app_mesh.types.gateway_route_spec
    import aws_sdk_app_mesh.types.resource_name


class UpdateGatewayRouteInput(TypedDict):
    gateway_route_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the gateway route to update.</p>"""
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the gateway route resides in.</p>"""
    virtual_gateway_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual gateway that the gateway route is associated with.</p>"""
    spec: "aws_sdk_app_mesh.types.gateway_route_spec.GatewayRouteSpec"
    """<p>The new gateway route specification to apply. This overwrites the existing data.</p>"""
    client_token: NotRequired["str"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>"""
    mesh_owner: NotRequired["aws_sdk_app_mesh.types.account_id.AccountId"]
    r"""<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRouteInput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.gateway_route_spec

    out["spec"] = aws_sdk_app_mesh.types.gateway_route_spec.serialize_json(
        value["spec"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayRouteInput:
    out: UpdateGatewayRouteInput = {}  # type: ignore[typeddict-item]
    if "spec" in data:
        import aws_sdk_app_mesh.types.gateway_route_spec

        out["spec"] = aws_sdk_app_mesh.types.gateway_route_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("UpdateGatewayRouteInput.spec required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
