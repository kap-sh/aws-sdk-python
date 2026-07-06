"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTimeout``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.grpc_timeout
    import aws_sdk_app_mesh.types.http_timeout
    import aws_sdk_app_mesh.types.tcp_timeout


class _ListenerTimeout_tcp(TypedDict, closed=True):
    tcp: "aws_sdk_app_mesh.types.tcp_timeout.TcpTimeout"


class _ListenerTimeout_http(TypedDict, closed=True):
    http: "aws_sdk_app_mesh.types.http_timeout.HttpTimeout"


class _ListenerTimeout_http2(TypedDict, closed=True):
    http2: "aws_sdk_app_mesh.types.http_timeout.HttpTimeout"


class _ListenerTimeout_grpc(TypedDict, closed=True):
    grpc: "aws_sdk_app_mesh.types.grpc_timeout.GrpcTimeout"


ListenerTimeout: TypeAlias = (
    _ListenerTimeout_tcp
    | _ListenerTimeout_http
    | _ListenerTimeout_http2
    | _ListenerTimeout_grpc
)


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTimeout) -> dict:
    if "tcp" in value:
        import aws_sdk_app_mesh.types.tcp_timeout

        return {"tcp": aws_sdk_app_mesh.types.tcp_timeout.serialize_json(value["tcp"])}
    elif "http" in value:
        import aws_sdk_app_mesh.types.http_timeout

        return {
            "http": aws_sdk_app_mesh.types.http_timeout.serialize_json(value["http"])
        }
    elif "http2" in value:
        import aws_sdk_app_mesh.types.http_timeout

        return {
            "http2": aws_sdk_app_mesh.types.http_timeout.serialize_json(value["http2"])
        }
    elif "grpc" in value:
        import aws_sdk_app_mesh.types.grpc_timeout

        return {
            "grpc": aws_sdk_app_mesh.types.grpc_timeout.serialize_json(value["grpc"])
        }
    else:
        raise SerializationError("ListenerTimeout: no variant present")


def deserialize_json(data: dict) -> ListenerTimeout:
    if "tcp" in data:
        import aws_sdk_app_mesh.types.tcp_timeout

        return {"tcp": aws_sdk_app_mesh.types.tcp_timeout.deserialize_json(data["tcp"])}
    elif "http" in data:
        import aws_sdk_app_mesh.types.http_timeout

        return {
            "http": aws_sdk_app_mesh.types.http_timeout.deserialize_json(data["http"])
        }
    elif "http2" in data:
        import aws_sdk_app_mesh.types.http_timeout

        return {
            "http2": aws_sdk_app_mesh.types.http_timeout.deserialize_json(data["http2"])
        }
    elif "grpc" in data:
        import aws_sdk_app_mesh.types.grpc_timeout

        return {
            "grpc": aws_sdk_app_mesh.types.grpc_timeout.deserialize_json(data["grpc"])
        }
    else:
        raise DeserializationError("ListenerTimeout: no recognized variant key")
