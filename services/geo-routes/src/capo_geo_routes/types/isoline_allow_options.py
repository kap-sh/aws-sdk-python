"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAllowOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_boolean


class IsolineAllowOptions(TypedDict, closed=True):
    hot: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>When true, allows the use of HOT (high-occupancy toll) lanes, which may affect travel times and reachable areas.</p> <p>Default value: <code>false</code> </p>"""
    hov: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>When true, allows the use of HOV (high-occupancy vehicle) lanes, which may affect travel times and reachable areas.</p> <p>Default value: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAllowOptions) -> dict:
    out: dict = {}
    if "hot" in value:
        out["Hot"] = value["hot"]
    if "hov" in value:
        out["Hov"] = value["hov"]
    return out


def deserialize_json(data: dict) -> IsolineAllowOptions:
    out: IsolineAllowOptions = {}  # type: ignore[typeddict-item]
    if "Hot" in data:
        out["hot"] = data["Hot"]
    if "Hov" in data:
        out["hov"] = data["Hov"]
    return out
