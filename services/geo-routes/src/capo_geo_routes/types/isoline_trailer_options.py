"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTrailerOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_integer


class IsolineTrailerOptions(TypedDict, closed=True):
    axle_count: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>The total number of axles across all trailers. Used for weight distribution calculations and road restrictions.</p>"""
    trailer_count: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>The number of trailers being pulled. Affects which roads can be used based on local regulations.</p> <p>Default value: <code>0</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTrailerOptions) -> dict:
    out: dict = {}
    if "axle_count" in value:
        out["AxleCount"] = value["axle_count"]
    if "trailer_count" in value:
        out["TrailerCount"] = value["trailer_count"]
    return out


def deserialize_json(data: dict) -> IsolineTrailerOptions:
    out: IsolineTrailerOptions = {}  # type: ignore[typeddict-item]
    if "AxleCount" in data:
        out["axle_count"] = data["AxleCount"]
    if "TrailerCount" in data:
        out["trailer_count"] = data["TrailerCount"]
    return out
