"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRouteMatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_hostname_match
    import aws_sdk_app_mesh.types.http_gateway_route_headers
    import aws_sdk_app_mesh.types.http_method
    import aws_sdk_app_mesh.types.http_path_match
    import aws_sdk_app_mesh.types.http_query_parameters
    import aws_sdk_app_mesh.types.listener_port


class HttpGatewayRouteMatch(TypedDict):
    prefix: NotRequired["str"]
    """<p>Specifies the path to match requests with. This parameter must always start with <code>/</code>, which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is <code>my-service.local</code> and you want the route to match requests to <code>my-service.local/metrics</code>, your prefix should be <code>/metrics</code>.</p>"""
    path: NotRequired["aws_sdk_app_mesh.types.http_path_match.HttpPathMatch"]
    """<p>The path to match on.</p>"""
    query_parameters: NotRequired[
        "aws_sdk_app_mesh.types.http_query_parameters.HttpQueryParameters"
    ]
    """<p>The query parameter to match on.</p>"""
    method: NotRequired["aws_sdk_app_mesh.types.http_method.HttpMethod"]
    """<p>The method to match on.</p>"""
    hostname: NotRequired[
        "aws_sdk_app_mesh.types.gateway_route_hostname_match.GatewayRouteHostnameMatch"
    ]
    """<p>The host name to match on.</p>"""
    headers: NotRequired[
        "aws_sdk_app_mesh.types.http_gateway_route_headers.HttpGatewayRouteHeaders"
    ]
    """<p>The client request headers to match on.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The port number to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRouteMatch) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    if "path" in value:
        import aws_sdk_app_mesh.types.http_path_match

        out["path"] = aws_sdk_app_mesh.types.http_path_match.serialize_json(
            value["path"]
        )
    if "query_parameters" in value:
        import aws_sdk_app_mesh.types.http_query_parameters

        out["queryParameters"] = (
            aws_sdk_app_mesh.types.http_query_parameters.serialize_json(
                value["query_parameters"]
            )
        )
    if "method" in value:
        out["method"] = value["method"]
    if "hostname" in value:
        import aws_sdk_app_mesh.types.gateway_route_hostname_match

        out["hostname"] = (
            aws_sdk_app_mesh.types.gateway_route_hostname_match.serialize_json(
                value["hostname"]
            )
        )
    if "headers" in value:
        import aws_sdk_app_mesh.types.http_gateway_route_headers

        out["headers"] = (
            aws_sdk_app_mesh.types.http_gateway_route_headers.serialize_json(
                value["headers"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> HttpGatewayRouteMatch:
    out: HttpGatewayRouteMatch = {}  # type: ignore[typeddict-item]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    if "path" in data:
        import aws_sdk_app_mesh.types.http_path_match

        out["path"] = aws_sdk_app_mesh.types.http_path_match.deserialize_json(
            data["path"]
        )
    if "queryParameters" in data:
        import aws_sdk_app_mesh.types.http_query_parameters

        out["query_parameters"] = (
            aws_sdk_app_mesh.types.http_query_parameters.deserialize_json(
                data["queryParameters"]
            )
        )
    if "method" in data:
        out["method"] = data["method"]
    if "hostname" in data:
        import aws_sdk_app_mesh.types.gateway_route_hostname_match

        out["hostname"] = (
            aws_sdk_app_mesh.types.gateway_route_hostname_match.deserialize_json(
                data["hostname"]
            )
        )
    if "headers" in data:
        import aws_sdk_app_mesh.types.http_gateway_route_headers

        out["headers"] = (
            aws_sdk_app_mesh.types.http_gateway_route_headers.deserialize_json(
                data["headers"]
            )
        )
    if "port" in data:
        out["port"] = data["port"]
    return out
