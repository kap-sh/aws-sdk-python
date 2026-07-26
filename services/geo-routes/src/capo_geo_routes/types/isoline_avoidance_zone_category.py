"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceZoneCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_zone_category


class IsolineAvoidanceZoneCategory(TypedDict, closed=True):
    category: NotRequired[
        "capo_geo_routes.types.isoline_zone_category.IsolineZoneCategory"
    ]
    """<p>The type of regulated zone: <code>CongestionPricing</code> for toll zones based on traffic levels, <code>Environmental</code> for low-emission zones, or <code>Vignette</code> for areas requiring special permits or stickers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceZoneCategory) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_geo_routes.types.isoline_zone_category

        out["Category"] = capo_geo_routes.types.isoline_zone_category.serialize_json(
            value["category"]
        )
    return out


def deserialize_json(data: dict) -> IsolineAvoidanceZoneCategory:
    out: IsolineAvoidanceZoneCategory = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import capo_geo_routes.types.isoline_zone_category

        out["category"] = capo_geo_routes.types.isoline_zone_category.deserialize_json(
            data["Category"]
        )
    return out
