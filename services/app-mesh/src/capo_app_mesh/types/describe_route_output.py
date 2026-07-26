"""Generated from Smithy shape ``com.amazonaws.appmesh#DescribeRouteOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.route_data


class DescribeRouteOutput(TypedDict, closed=True):
    route: "capo_app_mesh.types.route_data.RouteData"
    """<p>The full description of your route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRouteOutput) -> dict:
    out: dict = {}
    import capo_app_mesh.types.route_data

    out["route"] = capo_app_mesh.types.route_data.serialize_json(value["route"])
    return out


def deserialize_json(data: dict) -> DescribeRouteOutput:
    out: DescribeRouteOutput = {}  # type: ignore[typeddict-item]
    if "route" in data:
        import capo_app_mesh.types.route_data

        out["route"] = capo_app_mesh.types.route_data.deserialize_json(data["route"])
    else:
        raise DeserializationError("DescribeRouteOutput.route required")
    return out
