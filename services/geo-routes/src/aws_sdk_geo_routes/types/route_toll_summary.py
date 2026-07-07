"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_toll_price_summary


class RouteTollSummary(TypedDict, closed=True):
    total: NotRequired[
        "aws_sdk_geo_routes.types.route_toll_price_summary.RouteTollPriceSummary"
    ]
    """<p>Total toll summary for the complete route. Total is the only summary available today.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollSummary) -> dict:
    out: dict = {}
    if "total" in value:
        import aws_sdk_geo_routes.types.route_toll_price_summary

        out["Total"] = aws_sdk_geo_routes.types.route_toll_price_summary.serialize_json(
            value["total"]
        )
    return out


def deserialize_json(data: dict) -> RouteTollSummary:
    out: RouteTollSummary = {}  # type: ignore[typeddict-item]
    if "Total" in data:
        import aws_sdk_geo_routes.types.route_toll_price_summary

        out["total"] = (
            aws_sdk_geo_routes.types.route_toll_price_summary.deserialize_json(
                data["Total"]
            )
        )
    return out
