"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayHttp2ConnectionPool``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.max_requests


class VirtualGatewayHttp2ConnectionPool(TypedDict):
    max_requests: "aws_sdk_app_mesh.types.max_requests.MaxRequests"
    """<p>Maximum number of inflight requests Envoy can concurrently support across hosts in upstream cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayHttp2ConnectionPool) -> dict:
    out: dict = {}
    out["maxRequests"] = value["max_requests"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayHttp2ConnectionPool:
    out: VirtualGatewayHttp2ConnectionPool = {}  # type: ignore[typeddict-item]
    if "maxRequests" in data:
        out["max_requests"] = data["maxRequests"]
    else:
        raise DeserializationError(
            "VirtualGatewayHttp2ConnectionPool.max_requests required"
        )
    return out
