"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitAgency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTransitAgency(TypedDict, closed=True):
    name: "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Name of the agency.</p>"""
    url: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>URL to the agency's website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitAgency) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteTransitAgency:
    out: RouteTransitAgency = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RouteTransitAgency.name required")
    if "Url" in data:
        out["url"] = data["Url"]
    return out
