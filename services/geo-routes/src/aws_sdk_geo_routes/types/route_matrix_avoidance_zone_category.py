"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceZoneCategory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_zone_category


class RouteMatrixAvoidanceZoneCategory(TypedDict):
    category: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_zone_category.RouteMatrixZoneCategory"
    ]
    """<p>Zone category to be avoided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceZoneCategory) -> dict:
    out: dict = {}
    if "category" in value:
        import aws_sdk_geo_routes.types.route_matrix_zone_category

        out["Category"] = (
            aws_sdk_geo_routes.types.route_matrix_zone_category.serialize_json(
                value["category"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixAvoidanceZoneCategory:
    out: RouteMatrixAvoidanceZoneCategory = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_geo_routes.types.route_matrix_zone_category

        out["category"] = (
            aws_sdk_geo_routes.types.route_matrix_zone_category.deserialize_json(
                data["Category"]
            )
        )
    return out
