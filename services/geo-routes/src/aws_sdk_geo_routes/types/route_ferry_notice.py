"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryNotice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_ferry_notice_code
    import aws_sdk_geo_routes.types.route_notice_impact


class RouteFerryNotice(TypedDict):
    code: "aws_sdk_geo_routes.types.route_ferry_notice_code.RouteFerryNoticeCode"
    """<p>Code corresponding to the issue.</p>"""
    impact: NotRequired[
        "aws_sdk_geo_routes.types.route_notice_impact.RouteNoticeImpact"
    ]
    """<p>Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryNotice) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_ferry_notice_code

    out["Code"] = aws_sdk_geo_routes.types.route_ferry_notice_code.serialize_json(
        value["code"]
    )
    if "impact" in value:
        import aws_sdk_geo_routes.types.route_notice_impact

        out["Impact"] = aws_sdk_geo_routes.types.route_notice_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> RouteFerryNotice:
    out: RouteFerryNotice = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_geo_routes.types.route_ferry_notice_code

        out["code"] = aws_sdk_geo_routes.types.route_ferry_notice_code.deserialize_json(
            data["Code"]
        )
    else:
        raise DeserializationError("RouteFerryNotice.code required")
    if "Impact" in data:
        import aws_sdk_geo_routes.types.route_notice_impact

        out["impact"] = aws_sdk_geo_routes.types.route_notice_impact.deserialize_json(
            data["Impact"]
        )
    return out
