"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductLastModifiedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.saa_s_product_last_modified_date_filter_date_range


class SaaSProductLastModifiedDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.saa_s_product_last_modified_date_filter_date_range.SaaSProductLastModifiedDateFilterDateRange"
    ]
    """<p>Dates between which the SaaS product was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductLastModifiedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.saa_s_product_last_modified_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.saa_s_product_last_modified_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> SaaSProductLastModifiedDateFilter:
    out: SaaSProductLastModifiedDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import capo_marketplace_catalog.types.saa_s_product_last_modified_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.saa_s_product_last_modified_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
