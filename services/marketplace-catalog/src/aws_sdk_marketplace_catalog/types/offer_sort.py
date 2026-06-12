"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSort``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_sort_by
    import aws_sdk_marketplace_catalog.types.sort_order


class OfferSort(TypedDict):
    sort_by: NotRequired["aws_sdk_marketplace_catalog.types.offer_sort_by.OfferSortBy"]
    """<p>Allows to sort offers.</p>"""
    sort_order: NotRequired["aws_sdk_marketplace_catalog.types.sort_order.SortOrder"]
    """<p>Allows to sort offers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_marketplace_catalog.types.offer_sort_by

        out["SortBy"] = aws_sdk_marketplace_catalog.types.offer_sort_by.serialize_json(
            value["sort_by"]
        )
    if "sort_order" in value:
        import aws_sdk_marketplace_catalog.types.sort_order

        out["SortOrder"] = aws_sdk_marketplace_catalog.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> OfferSort:
    out: OfferSort = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_marketplace_catalog.types.offer_sort_by

        out["sort_by"] = (
            aws_sdk_marketplace_catalog.types.offer_sort_by.deserialize_json(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_marketplace_catalog.types.sort_order

        out["sort_order"] = (
            aws_sdk_marketplace_catalog.types.sort_order.deserialize_json(
                data["SortOrder"]
            )
        )
    return out
