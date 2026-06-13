"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeGatewayRouteOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_data


class DescribeGatewayRouteOutput(TypedDict):
    gateway_route: "aws_sdk_app_mesh.types.gateway_route_data.GatewayRouteData"
    """<p>The full description of your gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayRouteOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.gateway_route_data

    out["gatewayRoute"] = aws_sdk_app_mesh.types.gateway_route_data.serialize_json(
        value["gateway_route"]
    )
    return out


def deserialize_json(data: dict) -> DescribeGatewayRouteOutput:
    out: DescribeGatewayRouteOutput = {}  # type: ignore[typeddict-item]
    if "gatewayRoute" in data:
        import aws_sdk_app_mesh.types.gateway_route_data

        out["gateway_route"] = (
            aws_sdk_app_mesh.types.gateway_route_data.deserialize_json(
                data["gatewayRoute"]
            )
        )
    else:
        raise DeserializationError("DescribeGatewayRouteOutput.gateway_route required")
    return out
