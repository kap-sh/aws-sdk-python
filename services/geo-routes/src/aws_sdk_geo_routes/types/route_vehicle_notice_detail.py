"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_violated_constraints
    import aws_sdk_geo_routes.types.sensitive_string


class RouteVehicleNoticeDetail(TypedDict, closed=True):
    title: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The notice title.</p>"""
    violated_constraints: NotRequired[
        "aws_sdk_geo_routes.types.route_violated_constraints.RouteViolatedConstraints"
    ]
    """<p>Any violated constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNoticeDetail) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "violated_constraints" in value:
        import aws_sdk_geo_routes.types.route_violated_constraints

        out["ViolatedConstraints"] = (
            aws_sdk_geo_routes.types.route_violated_constraints.serialize_json(
                value["violated_constraints"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleNoticeDetail:
    out: RouteVehicleNoticeDetail = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    if "ViolatedConstraints" in data:
        import aws_sdk_geo_routes.types.route_violated_constraints

        out["violated_constraints"] = (
            aws_sdk_geo_routes.types.route_violated_constraints.deserialize_json(
                data["ViolatedConstraints"]
            )
        )
    return out
