"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateDirectConnectGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_id
    import aws_sdk_direct_connect.types.direct_connect_gateway_name


class UpdateDirectConnectGatewayRequest(TypedDict):
    direct_connect_gateway_id: (
        "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway to update.</p>"""
    new_direct_connect_gateway_name: "aws_sdk_direct_connect.types.direct_connect_gateway_name.DirectConnectGatewayName"
    """<p>The new name for the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectConnectGatewayRequest) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    out["newDirectConnectGatewayName"] = value["new_direct_connect_gateway_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDirectConnectGatewayRequest:
    out: UpdateDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        raise DeserializationError(
            "UpdateDirectConnectGatewayRequest.direct_connect_gateway_id required"
        )
    if "newDirectConnectGatewayName" in data:
        out["new_direct_connect_gateway_name"] = data["newDirectConnectGatewayName"]
    else:
        raise DeserializationError(
            "UpdateDirectConnectGatewayRequest.new_direct_connect_gateway_name required"
        )
    return out
