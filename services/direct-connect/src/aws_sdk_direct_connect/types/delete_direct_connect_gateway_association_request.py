"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_id
    import aws_sdk_direct_connect.types.direct_connect_gateway_id
    import aws_sdk_direct_connect.types.virtual_gateway_id


class DeleteDirectConnectGatewayAssociationRequest(TypedDict, closed=True):
    association_id: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
    ]
    """<p>The ID of the Direct Connect gateway association.</p>"""
    direct_connect_gateway_id: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    virtual_gateway_id: NotRequired[
        "aws_sdk_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDirectConnectGatewayAssociationRequest) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteDirectConnectGatewayAssociationRequest:
    out: DeleteDirectConnectGatewayAssociationRequest = {}  # type: ignore[typeddict-item]
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "virtualGatewayId" in data:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    return out
