"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTrailerOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_integer


class RouteTrailerOptions(TypedDict, closed=True):
    axle_count: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>Total number of axles of the vehicle.</p>"""
    trailer_count: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of trailers attached to the vehicle.</p> <p>Default value: <code>0</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTrailerOptions) -> dict:
    out: dict = {}
    if "axle_count" in value:
        out["AxleCount"] = value["axle_count"]
    if "trailer_count" in value:
        out["TrailerCount"] = value["trailer_count"]
    return out


def deserialize_json(data: dict) -> RouteTrailerOptions:
    out: RouteTrailerOptions = {}  # type: ignore[typeddict-item]
    if "AxleCount" in data:
        out["axle_count"] = data["AxleCount"]
    if "TrailerCount" in data:
        out["trailer_count"] = data["TrailerCount"]
    return out
