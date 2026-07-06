"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayHttpConnectionPool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.max_connections
    import aws_sdk_app_mesh.types.max_pending_requests


class VirtualGatewayHttpConnectionPool(TypedDict, closed=True):
    max_connections: "aws_sdk_app_mesh.types.max_connections.MaxConnections"
    """<p>Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.</p>"""
    max_pending_requests: NotRequired[
        "aws_sdk_app_mesh.types.max_pending_requests.MaxPendingRequests"
    ]
    """<p>Number of overflowing requests after <code>max_connections</code> Envoy will queue to upstream cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayHttpConnectionPool) -> dict:
    out: dict = {}
    out["maxConnections"] = value["max_connections"]
    if "max_pending_requests" in value:
        out["maxPendingRequests"] = value["max_pending_requests"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayHttpConnectionPool:
    out: VirtualGatewayHttpConnectionPool = {}  # type: ignore[typeddict-item]
    if "maxConnections" in data:
        out["max_connections"] = data["maxConnections"]
    else:
        raise DeserializationError(
            "VirtualGatewayHttpConnectionPool.max_connections required"
        )
    if "maxPendingRequests" in data:
        out["max_pending_requests"] = data["maxPendingRequests"]
    return out
