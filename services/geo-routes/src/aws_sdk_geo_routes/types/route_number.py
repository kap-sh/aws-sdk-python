"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteNumber``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.language_tag
    import aws_sdk_geo_routes.types.route_direction
    import aws_sdk_geo_routes.types.sensitive_string


class RouteNumber(TypedDict, closed=True):
    direction: NotRequired["aws_sdk_geo_routes.types.route_direction.RouteDirection"]
    """<p>Directional identifier of the route.</p>"""
    language: NotRequired["aws_sdk_geo_routes.types.language_tag.LanguageTag"]
    """<p>List of languages for instructions corresponding to the route number.</p>"""
    value: "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    """<p>The route number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteNumber) -> dict:
    out: dict = {}
    if "direction" in value:
        import aws_sdk_geo_routes.types.route_direction

        out["Direction"] = aws_sdk_geo_routes.types.route_direction.serialize_json(
            value["direction"]
        )
    if "language" in value:
        out["Language"] = value["language"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> RouteNumber:
    out: RouteNumber = {}  # type: ignore[typeddict-item]
    if "Direction" in data:
        import aws_sdk_geo_routes.types.route_direction

        out["direction"] = aws_sdk_geo_routes.types.route_direction.deserialize_json(
            data["Direction"]
        )
    if "Language" in data:
        out["language"] = data["Language"]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("RouteNumber.value required")
    return out
