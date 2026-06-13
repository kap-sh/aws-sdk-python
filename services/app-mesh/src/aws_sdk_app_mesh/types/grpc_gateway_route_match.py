"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcGatewayRouteMatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_hostname_match
    import aws_sdk_app_mesh.types.grpc_gateway_route_metadata_list
    import aws_sdk_app_mesh.types.listener_port
    import aws_sdk_app_mesh.types.service_name


class GrpcGatewayRouteMatch(TypedDict):
    service_name: NotRequired["aws_sdk_app_mesh.types.service_name.ServiceName"]
    """<p>The fully qualified domain name for the service to match from the request.</p>"""
    hostname: NotRequired[
        "aws_sdk_app_mesh.types.gateway_route_hostname_match.GatewayRouteHostnameMatch"
    ]
    """<p>The gateway route host name to be matched on.</p>"""
    metadata: NotRequired[
        "aws_sdk_app_mesh.types.grpc_gateway_route_metadata_list.GrpcGatewayRouteMetadataList"
    ]
    """<p>The gateway route metadata to be matched on.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The gateway route port to be matched on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcGatewayRouteMatch) -> dict:
    out: dict = {}
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "hostname" in value:
        import aws_sdk_app_mesh.types.gateway_route_hostname_match

        out["hostname"] = (
            aws_sdk_app_mesh.types.gateway_route_hostname_match.serialize_json(
                value["hostname"]
            )
        )
    if "metadata" in value:
        import aws_sdk_app_mesh.types.grpc_gateway_route_metadata_list

        out["metadata"] = (
            aws_sdk_app_mesh.types.grpc_gateway_route_metadata_list.serialize_json(
                value["metadata"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> GrpcGatewayRouteMatch:
    out: GrpcGatewayRouteMatch = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "hostname" in data:
        import aws_sdk_app_mesh.types.gateway_route_hostname_match

        out["hostname"] = (
            aws_sdk_app_mesh.types.gateway_route_hostname_match.deserialize_json(
                data["hostname"]
            )
        )
    if "metadata" in data:
        import aws_sdk_app_mesh.types.grpc_gateway_route_metadata_list

        out["metadata"] = (
            aws_sdk_app_mesh.types.grpc_gateway_route_metadata_list.deserialize_json(
                data["metadata"]
            )
        )
    if "port" in data:
        out["port"] = data["port"]
    return out
