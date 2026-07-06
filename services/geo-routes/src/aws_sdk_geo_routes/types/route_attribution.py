"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAttribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_attribution_type
    import aws_sdk_geo_routes.types.route_web_link


class RouteAttribution(TypedDict, closed=True):
    attribution_type: NotRequired[
        "aws_sdk_geo_routes.types.route_attribution_type.RouteAttributionType"
    ]
    """<p>The type of the attribution link.</p>"""
    web_link: "aws_sdk_geo_routes.types.route_web_link.RouteWebLink"
    """<p>The URL to an external resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAttribution) -> dict:
    out: dict = {}
    if "attribution_type" in value:
        import aws_sdk_geo_routes.types.route_attribution_type

        out["AttributionType"] = (
            aws_sdk_geo_routes.types.route_attribution_type.serialize_json(
                value["attribution_type"]
            )
        )
    import aws_sdk_geo_routes.types.route_web_link

    out["WebLink"] = aws_sdk_geo_routes.types.route_web_link.serialize_json(
        value["web_link"]
    )
    return out


def deserialize_json(data: dict) -> RouteAttribution:
    out: RouteAttribution = {}  # type: ignore[typeddict-item]
    if "AttributionType" in data:
        import aws_sdk_geo_routes.types.route_attribution_type

        out["attribution_type"] = (
            aws_sdk_geo_routes.types.route_attribution_type.deserialize_json(
                data["AttributionType"]
            )
        )
    if "WebLink" in data:
        import aws_sdk_geo_routes.types.route_web_link

        out["web_link"] = aws_sdk_geo_routes.types.route_web_link.deserialize_json(
            data["WebLink"]
        )
    else:
        raise DeserializationError("RouteAttribution.web_link required")
    return out
