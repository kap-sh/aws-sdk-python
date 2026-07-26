"""Generated from Smithy shape ``com.amazonaws.appmesh#UpdateRouteOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.route_data


class UpdateRouteOutput(TypedDict, closed=True):
    route: "capo_app_mesh.types.route_data.RouteData"
    """<p>A full description of the route that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.route_data

    out["route"] = capo_app_mesh.types.route_data.serialize_json(value["route"])
    return out


def deserialize_json(data: dict) -> UpdateRouteOutput:
    out: UpdateRouteOutput = {}  # type: ignore[typeddict-item]
    if "route" in data:
        import capo_app_mesh.types.route_data

        out["route"] = capo_app_mesh.types.route_data.deserialize_json(data["route"])
    else:
        raise DeserializationError("UpdateRouteOutput.route required")
    return out
