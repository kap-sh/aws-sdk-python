"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRouteRewrite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_hostname_rewrite
    import aws_sdk_app_mesh.types.http_gateway_route_path_rewrite
    import aws_sdk_app_mesh.types.http_gateway_route_prefix_rewrite


class HttpGatewayRouteRewrite(TypedDict, closed=True):
    prefix: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route_prefix_rewrite.HttpGatewayRoutePrefixRewrite"
    ]
    """<p>The specified beginning characters to rewrite.</p>"""
    path: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route_path_rewrite.HttpGatewayRoutePathRewrite"
    ]
    """<p>The path to rewrite.</p>"""
    hostname: NotRequired[
        "aws_sdk_app_mesh.types.gateway_route_hostname_rewrite.GatewayRouteHostnameRewrite"
    ]
    """<p>The host name to rewrite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRouteRewrite) -> dict:
    out: dict = {}
    if "prefix" in value:
        import aws_sdk_app_mesh.types.http_gateway_route_prefix_rewrite

        out["prefix"] = (
            aws_sdk_app_mesh.types.http_gateway_route_prefix_rewrite.serialize_json(
                value["prefix"]
            )
        )
    if "path" in value:
        import aws_sdk_app_mesh.types.http_gateway_route_path_rewrite

        out["path"] = (
            aws_sdk_app_mesh.types.http_gateway_route_path_rewrite.serialize_json(
                value["path"]
            )
        )
    if "hostname" in value:
        import aws_sdk_app_mesh.types.gateway_route_hostname_rewrite

        out["hostname"] = (
            aws_sdk_app_mesh.types.gateway_route_hostname_rewrite.serialize_json(
                value["hostname"]
            )
        )
    return out


def deserialize_json(data: dict) -> HttpGatewayRouteRewrite:
    out: HttpGatewayRouteRewrite = {}  # type: ignore[typeddict-item]
    if "prefix" in data:
        import aws_sdk_app_mesh.types.http_gateway_route_prefix_rewrite

        out["prefix"] = (
            aws_sdk_app_mesh.types.http_gateway_route_prefix_rewrite.deserialize_json(
                data["prefix"]
            )
        )
    if "path" in data:
        import aws_sdk_app_mesh.types.http_gateway_route_path_rewrite

        out["path"] = (
            aws_sdk_app_mesh.types.http_gateway_route_path_rewrite.deserialize_json(
                data["path"]
            )
        )
    if "hostname" in data:
        import aws_sdk_app_mesh.types.gateway_route_hostname_rewrite

        out["hostname"] = (
            aws_sdk_app_mesh.types.gateway_route_hostname_rewrite.deserialize_json(
                data["hostname"]
            )
        )
    return out
