"""Generated from Smithy shape ``com.amazonaws.appmesh#TcpRouteMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.listener_port


class TcpRouteMatch(TypedDict, closed=True):
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The port number to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TcpRouteMatch) -> dict:
    out: dict = {}
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> TcpRouteMatch:
    out: TcpRouteMatch = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    return out
