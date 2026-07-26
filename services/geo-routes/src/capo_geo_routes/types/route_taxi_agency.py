"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiAgency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class RouteTaxiAgency(TypedDict, closed=True):
    name: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Name of the agency.</p>"""
    url: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>URL to the agency's website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiAgency) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteTaxiAgency:
    out: RouteTaxiAgency = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RouteTaxiAgency.name required")
    if "Url" in data:
        out["url"] = data["Url"]
    return out
