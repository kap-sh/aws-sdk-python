"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductLastModifiedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.container_product_last_modified_date_filter_date_range


class ContainerProductLastModifiedDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.container_product_last_modified_date_filter_date_range.ContainerProductLastModifiedDateFilterDateRange"
    ]
    """<p>Dates between which the container product was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductLastModifiedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.container_product_last_modified_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.container_product_last_modified_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerProductLastModifiedDateFilter:
    out: ContainerProductLastModifiedDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import capo_marketplace_catalog.types.container_product_last_modified_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.container_product_last_modified_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
