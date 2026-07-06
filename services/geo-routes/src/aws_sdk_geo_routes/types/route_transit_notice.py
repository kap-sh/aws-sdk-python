"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNotice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_notice_impact
    import aws_sdk_geo_routes.types.route_transit_notice_code


class RouteTransitNotice(TypedDict, closed=True):
    code: "aws_sdk_geo_routes.types.route_transit_notice_code.RouteTransitNoticeCode"
    """<p>Code corresponding to the issue.</p>"""
    impact: NotRequired[
        "aws_sdk_geo_routes.types.route_notice_impact.RouteNoticeImpact"
    ]
    """<p>Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitNotice) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_transit_notice_code

    out["Code"] = aws_sdk_geo_routes.types.route_transit_notice_code.serialize_json(
        value["code"]
    )
    if "impact" in value:
        import aws_sdk_geo_routes.types.route_notice_impact

        out["Impact"] = aws_sdk_geo_routes.types.route_notice_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> RouteTransitNotice:
    out: RouteTransitNotice = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_geo_routes.types.route_transit_notice_code

        out["code"] = (
            aws_sdk_geo_routes.types.route_transit_notice_code.deserialize_json(
                data["Code"]
            )
        )
    else:
        raise DeserializationError("RouteTransitNotice.code required")
    if "Impact" in data:
        import aws_sdk_geo_routes.types.route_notice_impact

        out["impact"] = aws_sdk_geo_routes.types.route_notice_impact.deserialize_json(
            data["Impact"]
        )
    return out
