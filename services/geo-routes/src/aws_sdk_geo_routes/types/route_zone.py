"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_zone_category
    import aws_sdk_geo_routes.types.sensitive_string


class RouteZone(TypedDict, closed=True):
    category: NotRequired[
        "aws_sdk_geo_routes.types.route_zone_category.RouteZoneCategory"
    ]
    """<p>The zone category.</p>"""
    name: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteZone) -> dict:
    out: dict = {}
    if "category" in value:
        import aws_sdk_geo_routes.types.route_zone_category

        out["Category"] = aws_sdk_geo_routes.types.route_zone_category.serialize_json(
            value["category"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> RouteZone:
    out: RouteZone = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_geo_routes.types.route_zone_category

        out["category"] = aws_sdk_geo_routes.types.route_zone_category.deserialize_json(
            data["Category"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
