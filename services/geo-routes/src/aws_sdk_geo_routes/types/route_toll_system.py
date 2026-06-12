"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollSystem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTollSystem(TypedDict):
    name: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The toll system name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollSystem) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> RouteTollSystem:
    out: RouteTollSystem = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
