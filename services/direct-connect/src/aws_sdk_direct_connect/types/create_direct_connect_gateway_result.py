"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateDirectConnectGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway


class CreateDirectConnectGatewayResult(TypedDict):
    direct_connect_gateway: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway.DirectConnectGateway"
    ]
    """<p>The Direct Connect gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectConnectGatewayResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway

        out["directConnectGateway"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway.serialize_aws_json_1_1(
                value["direct_connect_gateway"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDirectConnectGatewayResult:
    out: CreateDirectConnectGatewayResult = {}  # type: ignore[typeddict-item]
    if "directConnectGateway" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway

        out["direct_connect_gateway"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway.deserialize_aws_json_1_1(
                data["directConnectGateway"]
            )
        )
    return out
