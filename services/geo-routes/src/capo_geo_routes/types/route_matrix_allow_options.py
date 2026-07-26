"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAllowOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_boolean


class RouteMatrixAllowOptions(TypedDict, closed=True):
    hot: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Allow Hot (High Occupancy Toll) lanes while calculating the route.</p> <p>Default value: <code>false</code> </p>"""
    hov: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Allow Hov (High Occupancy vehicle) lanes while calculating the route.</p> <p>Default value: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAllowOptions) -> dict:
    out: dict = {}
    if "hot" in value:
        out["Hot"] = value["hot"]
    if "hov" in value:
        out["Hov"] = value["hov"]
    return out


def deserialize_json(data: dict) -> RouteMatrixAllowOptions:
    out: RouteMatrixAllowOptions = {}  # type: ignore[typeddict-item]
    if "Hot" in data:
        out["hot"] = data["Hot"]
    if "Hov" in data:
        out["hov"] = data["Hov"]
    return out
