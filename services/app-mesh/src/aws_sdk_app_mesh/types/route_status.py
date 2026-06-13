"""Generated from Smithy shape ``com.amazonaws.appmesh#RouteStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.route_status_code


class RouteStatus(TypedDict):
    status: "aws_sdk_app_mesh.types.route_status_code.RouteStatusCode"
    """<p>The current status for the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> RouteStatus:
    out: RouteStatus = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("RouteStatus.status required")
    return out
