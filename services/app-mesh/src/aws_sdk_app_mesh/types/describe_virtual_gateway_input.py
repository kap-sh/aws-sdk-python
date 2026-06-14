"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeVirtualGatewayInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.account_id
    import aws_sdk_app_mesh.types.resource_name


class DescribeVirtualGatewayInput(TypedDict):
    virtual_gateway_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual gateway to describe.</p>"""
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the gateway route resides in.</p>"""
    mesh_owner: NotRequired["aws_sdk_app_mesh.types.account_id.AccountId"]
    r"""<p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href=\"https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html\">Working with shared meshes</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVirtualGatewayInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVirtualGatewayInput:
    out: DescribeVirtualGatewayInput = {}  # type: ignore[typeddict-item]
    return out
