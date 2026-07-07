"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeGatewayRouteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.account_id
    import aws_sdk_app_mesh.types.resource_name


class DescribeGatewayRouteInput(TypedDict, closed=True):
    gateway_route_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the gateway route to describe.</p>"""
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the gateway route resides in.</p>"""
    virtual_gateway_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual gateway that the gateway route is associated with.</p>"""
    mesh_owner: NotRequired["aws_sdk_app_mesh.types.account_id.AccountId"]
    r"""<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayRouteInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayRouteInput:
    out: DescribeGatewayRouteInput = {}  # type: ignore[typeddict-item]
    return out
