"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixOrigin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.route_matrix_origin_options


class RouteMatrixOrigin(TypedDict, closed=True):
    options: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_origin_options.RouteMatrixOriginOptions"
    ]
    r"""<p> Origin related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""
    position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixOrigin) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_geo_routes.types.route_matrix_origin_options

        out["Options"] = (
            aws_sdk_geo_routes.types.route_matrix_origin_options.serialize_json(
                value["options"]
            )
        )
    import aws_sdk_geo_routes.types.position

    out["Position"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["position"]
    )
    return out


def deserialize_json(data: dict) -> RouteMatrixOrigin:
    out: RouteMatrixOrigin = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_geo_routes.types.route_matrix_origin_options

        out["options"] = (
            aws_sdk_geo_routes.types.route_matrix_origin_options.deserialize_json(
                data["Options"]
            )
        )
    if "Position" in data:
        import aws_sdk_geo_routes.types.position

        out["position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteMatrixOrigin.position required")
    return out
