"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateGatewayRouteOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_data


class UpdateGatewayRouteOutput(TypedDict, closed=True):
    gateway_route: "capo_app_mesh.types.gateway_route_data.GatewayRouteData"
    """<p>A full description of the gateway route that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayRouteOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.gateway_route_data

    out["gatewayRoute"] = capo_app_mesh.types.gateway_route_data.serialize_json(
        value["gateway_route"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGatewayRouteOutput:
    out: UpdateGatewayRouteOutput = {}  # type: ignore[typeddict-item]
    if "gatewayRoute" in data:
        import capo_app_mesh.types.gateway_route_data

        out["gateway_route"] = capo_app_mesh.types.gateway_route_data.deserialize_json(
            data["gatewayRoute"]
        )
    else:
        raise DeserializationError("UpdateGatewayRouteOutput.gateway_route required")
    return out
