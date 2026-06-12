"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNotice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_notice_impact
    import aws_sdk_geo_routes.types.route_vehicle_notice_code
    import aws_sdk_geo_routes.types.route_vehicle_notice_detail_list


class RouteVehicleNotice(TypedDict):
    code: "aws_sdk_geo_routes.types.route_vehicle_notice_code.RouteVehicleNoticeCode"
    """<p>Code corresponding to the issue.</p>"""
    details: "aws_sdk_geo_routes.types.route_vehicle_notice_detail_list.RouteVehicleNoticeDetailList"
    """<p>Additional details of the notice.</p>"""
    impact: NotRequired[
        "aws_sdk_geo_routes.types.route_notice_impact.RouteNoticeImpact"
    ]
    """<p>Impact corresponding to the issue. While Low impact notices can be safely ignored, High impact notices must be evaluated further to determine the impact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNotice) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_vehicle_notice_code

    out["Code"] = aws_sdk_geo_routes.types.route_vehicle_notice_code.serialize_json(
        value["code"]
    )
    import aws_sdk_geo_routes.types.route_vehicle_notice_detail_list

    out["Details"] = (
        aws_sdk_geo_routes.types.route_vehicle_notice_detail_list.serialize_json(
            value["details"]
        )
    )
    if "impact" in value:
        import aws_sdk_geo_routes.types.route_notice_impact

        out["Impact"] = aws_sdk_geo_routes.types.route_notice_impact.serialize_json(
            value["impact"]
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleNotice:
    out: RouteVehicleNotice = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_geo_routes.types.route_vehicle_notice_code

        out["code"] = (
            aws_sdk_geo_routes.types.route_vehicle_notice_code.deserialize_json(
                data["Code"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleNotice.code required")
    if "Details" in data:
        import aws_sdk_geo_routes.types.route_vehicle_notice_detail_list

        out["details"] = (
            aws_sdk_geo_routes.types.route_vehicle_notice_detail_list.deserialize_json(
                data["Details"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleNotice.details required")
    if "Impact" in data:
        import aws_sdk_geo_routes.types.route_notice_impact

        out["impact"] = aws_sdk_geo_routes.types.route_notice_impact.deserialize_json(
            data["Impact"]
        )
    return out
