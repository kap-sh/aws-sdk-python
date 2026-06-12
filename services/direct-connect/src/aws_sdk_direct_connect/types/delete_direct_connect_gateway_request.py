"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_id


class DeleteDirectConnectGatewayRequest(TypedDict):
    direct_connect_gateway_id: (
        "aws_sdk_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    )
    """<p>The ID of the Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDirectConnectGatewayRequest) -> dict:
    out: dict = {}
    out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDirectConnectGatewayRequest:
    out: DeleteDirectConnectGatewayRequest = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    else:
        raise DeserializationError(
            "DeleteDirectConnectGatewayRequest.direct_connect_gateway_id required"
        )
    return out
