"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferAvailabilityEndDateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter_date_range


class OfferAvailabilityEndDateFilter(TypedDict):
    date_range: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter_date_range.OfferAvailabilityEndDateFilterDateRange"
    ]
    """<p>Allows filtering on the <code>AvailabilityEndDate</code> of an offer with date range as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferAvailabilityEndDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter_date_range

        out["DateRange"] = (
            aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferAvailabilityEndDateFilter:
    out: OfferAvailabilityEndDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter_date_range

        out["date_range"] = (
            aws_sdk_marketplace_catalog.types.offer_availability_end_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
