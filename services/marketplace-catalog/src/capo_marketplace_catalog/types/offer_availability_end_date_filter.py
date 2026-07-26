"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferAvailabilityEndDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_availability_end_date_filter_date_range


class OfferAvailabilityEndDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.offer_availability_end_date_filter_date_range.OfferAvailabilityEndDateFilterDateRange"
    ]
    """<p>Allows filtering on the <code>AvailabilityEndDate</code> of an offer with date range as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferAvailabilityEndDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.offer_availability_end_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.offer_availability_end_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferAvailabilityEndDateFilter:
    out: OfferAvailabilityEndDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import capo_marketplace_catalog.types.offer_availability_end_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.offer_availability_end_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
