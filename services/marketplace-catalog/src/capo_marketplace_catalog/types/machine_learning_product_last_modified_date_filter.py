"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductLastModifiedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.machine_learning_product_last_modified_date_filter_date_range


class MachineLearningProductLastModifiedDateFilter(TypedDict, closed=True):
    date_range: NotRequired[
        "capo_marketplace_catalog.types.machine_learning_product_last_modified_date_filter_date_range.MachineLearningProductLastModifiedDateFilterDateRange"
    ]
    """<p>A date range to filter by. The operation returns machine learning products with last modified dates that fall within this range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductLastModifiedDateFilter) -> dict:
    out: dict = {}
    if "date_range" in value:
        import capo_marketplace_catalog.types.machine_learning_product_last_modified_date_filter_date_range

        out["DateRange"] = (
            capo_marketplace_catalog.types.machine_learning_product_last_modified_date_filter_date_range.serialize_json(
                value["date_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> MachineLearningProductLastModifiedDateFilter:
    out: MachineLearningProductLastModifiedDateFilter = {}  # type: ignore[typeddict-item]
    if "DateRange" in data:
        import capo_marketplace_catalog.types.machine_learning_product_last_modified_date_filter_date_range

        out["date_range"] = (
            capo_marketplace_catalog.types.machine_learning_product_last_modified_date_filter_date_range.deserialize_json(
                data["DateRange"]
            )
        )
    return out
