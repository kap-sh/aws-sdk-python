"""Generated from Smithy shape ``com.amazonaws.groundstation#TimeAzEl``."""

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError


class TimeAzEl(TypedDict, closed=True):
    dt: "float"
    """<p>Time offset in atomic seconds from the segment's reference epoch.</p> <p>All <code>dt</code> values within a segment must be in ascending order with no duplicates.</p> <p> <code>dt</code> values may be:</p> <ul> <li> <p>negative</p> </li> <li> <p>expressed as fractions of a second</p> </li> <li> <p>expressed in scientific notation</p> </li> </ul>"""
    az: "float"
    """<p>Azimuth angle at the specified time.</p> <p>Valid ranges by unit:</p> <ul> <li> <p> <code>DEGREE_ANGLE</code>: -180 to 360 degrees, measured clockwise from true north</p> </li> <li> <p> <code>RADIAN</code>: -π to 2π radians, measured clockwise from true north</p> </li> </ul>"""
    el: "float"
    """<p>Elevation angle at the specified time.</p> <p>Valid ranges by unit:</p> <ul> <li> <p> <code>DEGREE_ANGLE</code>: -90 to 90 degrees, where 0 is the horizon, 90 is zenith, and negative values are below the horizon </p> </li> <li> <p> <code>RADIAN</code>: -π/2 to π/2 radians, where 0 is the horizon, π/2 is zenith, and negative values are below the horizon </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeAzEl) -> dict:
    out: dict = {}
    out["dt"] = value["dt"]
    out["az"] = value["az"]
    out["el"] = value["el"]
    return out


def deserialize_json(data: dict) -> TimeAzEl:
    out: TimeAzEl = {}  # type: ignore[typeddict-item]
    if "dt" in data:
        out["dt"] = data["dt"]
    else:
        raise DeserializationError("TimeAzEl.dt required")
    if "az" in data:
        out["az"] = data["az"]
    else:
        raise DeserializationError("TimeAzEl.az required")
    if "el" in data:
        out["el"] = data["el"]
    else:
        raise DeserializationError("TimeAzEl.el required")
    return out
