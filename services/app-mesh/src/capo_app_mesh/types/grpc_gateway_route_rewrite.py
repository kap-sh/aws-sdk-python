"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcGatewayRouteRewrite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_hostname_rewrite


class GrpcGatewayRouteRewrite(TypedDict, closed=True):
    hostname: NotRequired[
        "capo_app_mesh.types.gateway_route_hostname_rewrite.GatewayRouteHostnameRewrite"
    ]
    """<p>The host name of the gateway route to rewrite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcGatewayRouteRewrite) -> dict:
    out: dict = {}
    if "hostname" in value:
        import capo_app_mesh.types.gateway_route_hostname_rewrite

        out["hostname"] = (
            capo_app_mesh.types.gateway_route_hostname_rewrite.serialize_json(
                value["hostname"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrpcGatewayRouteRewrite:
    out: GrpcGatewayRouteRewrite = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        import capo_app_mesh.types.gateway_route_hostname_rewrite

        out["hostname"] = (
            capo_app_mesh.types.gateway_route_hostname_rewrite.deserialize_json(
                data["hostname"]
            )
        )
    return out
