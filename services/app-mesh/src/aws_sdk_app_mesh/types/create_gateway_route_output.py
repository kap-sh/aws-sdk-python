"""Generated from Smithy shape ``com.amazonaws.appmesh#CreateGatewayRouteOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_data


class CreateGatewayRouteOutput(TypedDict):
    gateway_route: "aws_sdk_app_mesh.types.gateway_route_data.GatewayRouteData"
    """<p>The full description of your gateway route following the create call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRouteOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.gateway_route_data

    out["gatewayRoute"] = aws_sdk_app_mesh.types.gateway_route_data.serialize_json(
        value["gateway_route"]
    )
    return out


def deserialize_json(data: dict) -> CreateGatewayRouteOutput:
    out: CreateGatewayRouteOutput = {}  # type: ignore[typeddict-item]
    if "gatewayRoute" in data:
        import aws_sdk_app_mesh.types.gateway_route_data

        out["gateway_route"] = (
            aws_sdk_app_mesh.types.gateway_route_data.deserialize_json(
                data["gatewayRoute"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRouteOutput.gateway_route required")
    return out
