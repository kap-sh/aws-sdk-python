"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayConnectionPool``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_grpc_connection_pool
    import aws_sdk_app_mesh.types.virtual_gateway_http2_connection_pool
    import aws_sdk_app_mesh.types.virtual_gateway_http_connection_pool


class _VirtualGatewayConnectionPool_http(TypedDict):
    http: "aws_sdk_app_mesh.types.virtual_gateway_http_connection_pool.VirtualGatewayHttpConnectionPool"


class _VirtualGatewayConnectionPool_http2(TypedDict):
    http2: "aws_sdk_app_mesh.types.virtual_gateway_http2_connection_pool.VirtualGatewayHttp2ConnectionPool"


class _VirtualGatewayConnectionPool_grpc(TypedDict):
    grpc: "aws_sdk_app_mesh.types.virtual_gateway_grpc_connection_pool.VirtualGatewayGrpcConnectionPool"


VirtualGatewayConnectionPool: TypeAlias = (
    _VirtualGatewayConnectionPool_http
    | _VirtualGatewayConnectionPool_http2
    | _VirtualGatewayConnectionPool_grpc
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayConnectionPool) -> dict:
    if "http" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_http_connection_pool

        return {
            "http": aws_sdk_app_mesh.types.virtual_gateway_http_connection_pool.serialize_json(
                value["http"]
            )
        }
    elif "http2" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_http2_connection_pool

        return {
            "http2": aws_sdk_app_mesh.types.virtual_gateway_http2_connection_pool.serialize_json(
                value["http2"]
            )
        }
    elif "grpc" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_grpc_connection_pool

        return {
            "grpc": aws_sdk_app_mesh.types.virtual_gateway_grpc_connection_pool.serialize_json(
                value["grpc"]
            )
        }
    else:
        raise SerializationError("VirtualGatewayConnectionPool: no variant present")


def deserialize_json(data: dict) -> VirtualGatewayConnectionPool:
    if "http" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_http_connection_pool

        return {
            "http": aws_sdk_app_mesh.types.virtual_gateway_http_connection_pool.deserialize_json(
                data["http"]
            )
        }
    elif "http2" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_http2_connection_pool

        return {
            "http2": aws_sdk_app_mesh.types.virtual_gateway_http2_connection_pool.deserialize_json(
                data["http2"]
            )
        }
    elif "grpc" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_grpc_connection_pool

        return {
            "grpc": aws_sdk_app_mesh.types.virtual_gateway_grpc_connection_pool.deserialize_json(
                data["grpc"]
            )
        }
    else:
        raise DeserializationError(
            "VirtualGatewayConnectionPool: no recognized variant key"
        )
