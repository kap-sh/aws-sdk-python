"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationRestProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class WaypointOptimizationRestProfile(TypedDict, closed=True):
    profile: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Pre defined rest profiles for a driver schedule. The only currently supported profile is EU.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationRestProfile) -> dict:
    out: dict = {}
    out["Profile"] = value["profile"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationRestProfile:
    out: WaypointOptimizationRestProfile = {}  # type: ignore[typeddict-item]
    if "Profile" in data:
        out["profile"] = data["Profile"]
    else:
        raise DeserializationError("WaypointOptimizationRestProfile.profile required")
    return out
