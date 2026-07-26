"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteGatewayRouteOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_data


class DeleteGatewayRouteOutput(TypedDict, closed=True):
    gateway_route: "capo_app_mesh.types.gateway_route_data.GatewayRouteData"
    """<p>The gateway route that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRouteOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.gateway_route_data

    out["gatewayRoute"] = capo_app_mesh.types.gateway_route_data.serialize_json(
        value["gateway_route"]
    )
    return out


def deserialize_json(data: dict) -> DeleteGatewayRouteOutput:
    out: DeleteGatewayRouteOutput = {}  # type: ignore[typeddict-item]
    if "gatewayRoute" in data:
        import capo_app_mesh.types.gateway_route_data

        out["gateway_route"] = capo_app_mesh.types.gateway_route_data.deserialize_json(
            data["gatewayRoute"]
        )
    else:
        raise DeserializationError("DeleteGatewayRouteOutput.gateway_route required")
    return out
