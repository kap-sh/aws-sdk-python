"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSignpostLabel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string
    import aws_sdk_geo_routes.types.route_number


class RouteSignpostLabel(TypedDict):
    route_number: NotRequired["aws_sdk_geo_routes.types.route_number.RouteNumber"]
    """<p>Route number of the road.</p>"""
    text: NotRequired["aws_sdk_geo_routes.types.localized_string.LocalizedString"]
    """<p>The Signpost text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSignpostLabel) -> dict:
    out: dict = {}
    if "route_number" in value:
        import aws_sdk_geo_routes.types.route_number

        out["RouteNumber"] = aws_sdk_geo_routes.types.route_number.serialize_json(
            value["route_number"]
        )
    if "text" in value:
        import aws_sdk_geo_routes.types.localized_string

        out["Text"] = aws_sdk_geo_routes.types.localized_string.serialize_json(
            value["text"]
        )
    return out


def deserialize_json(data: dict) -> RouteSignpostLabel:
    out: RouteSignpostLabel = {}  # type: ignore[typeddict-item]
    if "RouteNumber" in data:
        import aws_sdk_geo_routes.types.route_number

        out["route_number"] = aws_sdk_geo_routes.types.route_number.deserialize_json(
            data["RouteNumber"]
        )
    if "Text" in data:
        import aws_sdk_geo_routes.types.localized_string

        out["text"] = aws_sdk_geo_routes.types.localized_string.deserialize_json(
            data["Text"]
        )
    return out
