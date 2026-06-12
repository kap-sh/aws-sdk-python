"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferLastModifiedDateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter_date_range


class OfferLastModifiedDateFilter(TypedDict):
    date_range: NotRequired[
        "aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter_date_range.OfferLastModifiedDateFilterDateRange"
    ]
    """<p>Allows filtering on the <code>LastModifiedDate</code> of an offer with date range as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferLastModifiedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter_date_range

        out["DateRange"] = (
            aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferLastModifiedDateFilter:
    out: OfferLastModifiedDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter_date_range

        out["date_range"] = (
            aws_sdk_marketplace_catalog.types.offer_last_modified_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
