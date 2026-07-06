"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRouteMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.http_method
    import aws_sdk_app_mesh.types.http_path_match
    import aws_sdk_app_mesh.types.http_query_parameters
    import aws_sdk_app_mesh.types.http_route_headers
    import aws_sdk_app_mesh.types.http_scheme
    import aws_sdk_app_mesh.types.listener_port


class HttpRouteMatch(TypedDict, closed=True):
    prefix: NotRequired["str"]
    """<p>Specifies the path to match requests with. This parameter must always start with <code>/</code>, which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is <code>my-service.local</code> and you want the route to match requests to <code>my-service.local/metrics</code>, your prefix should be <code>/metrics</code>.</p>"""
    path: NotRequired["aws_sdk_app_mesh.types.http_path_match.HttpPathMatch"]
    """<p>The client request path to match on.</p>"""
    query_parameters: NotRequired[
        "aws_sdk_app_mesh.types.http_query_parameters.HttpQueryParameters"
    ]
    """<p>The client request query parameters to match on.</p>"""
    method: NotRequired["aws_sdk_app_mesh.types.http_method.HttpMethod"]
    """<p>The client request method to match on. Specify only one.</p>"""
    scheme: NotRequired["aws_sdk_app_mesh.types.http_scheme.HttpScheme"]
    """<p>The client request scheme to match on. Specify only one. Applicable only for HTTP2 routes.</p>"""
    headers: NotRequired["aws_sdk_app_mesh.types.http_route_headers.HttpRouteHeaders"]
    """<p>The client request headers to match on.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The port number to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRouteMatch) -> dict:
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
    if "scheme" in value:
        out["scheme"] = value["scheme"]
    if "headers" in value:
        import aws_sdk_app_mesh.types.http_route_headers

        out["headers"] = aws_sdk_app_mesh.types.http_route_headers.serialize_json(
            value["headers"]
        )
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> HttpRouteMatch:
    out: HttpRouteMatch = {}  # type: ignore[typeddict-item]
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
    if "scheme" in data:
        out["scheme"] = data["scheme"]
    if "headers" in data:
        import aws_sdk_app_mesh.types.http_route_headers

        out["headers"] = aws_sdk_app_mesh.types.http_route_headers.deserialize_json(
            data["headers"]
        )
    if "port" in data:
        out["port"] = data["port"]
    return out
