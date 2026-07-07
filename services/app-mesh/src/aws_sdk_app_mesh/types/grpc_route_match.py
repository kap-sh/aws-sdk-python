"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRouteMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.grpc_route_metadata_list
    import aws_sdk_app_mesh.types.listener_port
    import aws_sdk_app_mesh.types.method_name
    import aws_sdk_app_mesh.types.service_name


class GrpcRouteMatch(TypedDict, closed=True):
    service_name: NotRequired["aws_sdk_app_mesh.types.service_name.ServiceName"]
    """<p>The fully qualified domain name for the service to match from the request.</p>"""
    method_name: NotRequired["aws_sdk_app_mesh.types.method_name.MethodName"]
    """<p>The method name to match from the request. If you specify a name, you must also specify a <code>serviceName</code>.</p>"""
    metadata: NotRequired[
        "aws_sdk_app_mesh.types.grpc_route_metadata_list.GrpcRouteMetadataList"
    ]
    """<p>An object that represents the data to match from the request.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The port number to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRouteMatch) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "method_name" in value:
        out["methodName"] = value["method_name"]
    if "metadata" in value:
        import aws_sdk_app_mesh.types.grpc_route_metadata_list

        out["metadata"] = (
            aws_sdk_app_mesh.types.grpc_route_metadata_list.serialize_json(
                value["metadata"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> GrpcRouteMatch:
    out: GrpcRouteMatch = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "methodName" in data:
        out["method_name"] = data["methodName"]
    if "metadata" in data:
        import aws_sdk_app_mesh.types.grpc_route_metadata_list

        out["metadata"] = (
            aws_sdk_app_mesh.types.grpc_route_metadata_list.deserialize_json(
                data["metadata"]
            )
        )
    if "port" in data:
        out["port"] = data["port"]
    return out
