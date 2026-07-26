"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeConnectionPool``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_node_grpc_connection_pool
    import capo_app_mesh.types.virtual_node_http2_connection_pool
    import capo_app_mesh.types.virtual_node_http_connection_pool
    import capo_app_mesh.types.virtual_node_tcp_connection_pool


class _VirtualNodeConnectionPool_tcp(TypedDict, closed=True):
    tcp: "capo_app_mesh.types.virtual_node_tcp_connection_pool.VirtualNodeTcpConnectionPool"


class _VirtualNodeConnectionPool_http(TypedDict, closed=True):
    http: "capo_app_mesh.types.virtual_node_http_connection_pool.VirtualNodeHttpConnectionPool"


class _VirtualNodeConnectionPool_http2(TypedDict, closed=True):
    http2: "capo_app_mesh.types.virtual_node_http2_connection_pool.VirtualNodeHttp2ConnectionPool"


class _VirtualNodeConnectionPool_grpc(TypedDict, closed=True):
    grpc: "capo_app_mesh.types.virtual_node_grpc_connection_pool.VirtualNodeGrpcConnectionPool"


VirtualNodeConnectionPool: TypeAlias = (
    _VirtualNodeConnectionPool_tcp
    | _VirtualNodeConnectionPool_http
    | _VirtualNodeConnectionPool_http2
    | _VirtualNodeConnectionPool_grpc
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeConnectionPool) -> dict:
    if "tcp" in value:
        import capo_app_mesh.types.virtual_node_tcp_connection_pool

        return {
            "tcp": capo_app_mesh.types.virtual_node_tcp_connection_pool.serialize_json(
                value["tcp"]
            )
        }
    elif "http" in value:
        import capo_app_mesh.types.virtual_node_http_connection_pool

        return {
            "http": capo_app_mesh.types.virtual_node_http_connection_pool.serialize_json(
                value["http"]
            )
        }
    elif "http2" in value:
        import capo_app_mesh.types.virtual_node_http2_connection_pool

        return {
            "http2": capo_app_mesh.types.virtual_node_http2_connection_pool.serialize_json(
                value["http2"]
            )
        }
    elif "grpc" in value:
        import capo_app_mesh.types.virtual_node_grpc_connection_pool

        return {
            "grpc": capo_app_mesh.types.virtual_node_grpc_connection_pool.serialize_json(
                value["grpc"]
            )
        }
    else:
        raise SerializationError("VirtualNodeConnectionPool: no variant present")


def deserialize_json(data: dict) -> VirtualNodeConnectionPool:
    if "tcp" in data:
        import capo_app_mesh.types.virtual_node_tcp_connection_pool

        return {
            "tcp": capo_app_mesh.types.virtual_node_tcp_connection_pool.deserialize_json(
                data["tcp"]
            )
        }
    elif "http" in data:
        import capo_app_mesh.types.virtual_node_http_connection_pool

        return {
            "http": capo_app_mesh.types.virtual_node_http_connection_pool.deserialize_json(
                data["http"]
            )
        }
    elif "http2" in data:
        import capo_app_mesh.types.virtual_node_http2_connection_pool

        return {
            "http2": capo_app_mesh.types.virtual_node_http2_connection_pool.deserialize_json(
                data["http2"]
            )
        }
    elif "grpc" in data:
        import capo_app_mesh.types.virtual_node_grpc_connection_pool

        return {
            "grpc": capo_app_mesh.types.virtual_node_grpc_connection_pool.deserialize_json(
                data["grpc"]
            )
        }
    else:
        raise DeserializationError(
            "VirtualNodeConnectionPool: no recognized variant key"
        )
