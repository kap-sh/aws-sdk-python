"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAllowOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_boolean


class RouteAllowOptions(TypedDict):
    hot: NotRequired["aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Allow Hot (High Occupancy Toll) lanes while calculating the route.</p> <p>Default value: <code>false</code> </p>"""
    hov: NotRequired["aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Allow Hov (High Occupancy vehicle) lanes while calculating the route.</p> <p>Default value: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAllowOptions) -> dict:
    out: dict = {}
    if "hot" in value:
        out["Hot"] = value["hot"]
    if "hov" in value:
        out["Hov"] = value["hov"]
    return out


def deserialize_json(data: dict) -> RouteAllowOptions:
    out: RouteAllowOptions = {}  # type: ignore[typeddict-item]
    if "Hot" in data:
        out["hot"] = data["Hot"]
    if "Hov" in data:
        out["hov"] = data["Hov"]
    return out
