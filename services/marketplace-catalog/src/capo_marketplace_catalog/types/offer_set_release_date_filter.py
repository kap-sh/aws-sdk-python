"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetReleaseDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_set_release_date_filter_date_range


class OfferSetReleaseDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.offer_set_release_date_filter_date_range.OfferSetReleaseDateFilterDateRange"
    ]
    """<p>Allows filtering on the <code>ReleaseDate</code> of an offer set with date range as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetReleaseDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.offer_set_release_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.offer_set_release_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSetReleaseDateFilter:
    out: OfferSetReleaseDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import capo_marketplace_catalog.types.offer_set_release_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.offer_set_release_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
