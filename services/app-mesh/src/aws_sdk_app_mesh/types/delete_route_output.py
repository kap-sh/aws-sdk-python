"""Generated from Smithy shape ``com.amazonaws.appmesh#DeleteRouteOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.route_data

class DeleteRouteOutput(TypedDict):
    route: "aws_sdk_app_mesh.types.route_data.RouteData"
    """<p>The route that was deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouteOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.route_data
    out["route"] = aws_sdk_app_mesh.types.route_data.serialize_json(value["route"])
    return out


def deserialize_json(data: dict) -> DeleteRouteOutput:
    out: DeleteRouteOutput = {}  # type: ignore[typeddict-item]
    if "route" in data:
        import aws_sdk_app_mesh.types.route_data
        out["route"] = aws_sdk_app_mesh.types.route_data.deserialize_json(data["route"])
    else:
        raise DeserializationError("DeleteRouteOutput.route required")
    return out