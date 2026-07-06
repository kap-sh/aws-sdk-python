"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.data_product_sort_by
    import aws_sdk_marketplace_catalog.types.sort_order


class DataProductSort(TypedDict, closed=True):
    sort_by: NotRequired[
        "aws_sdk_marketplace_catalog.types.data_product_sort_by.DataProductSortBy"
    ]
    """<p>Field to sort the data products by.</p>"""
    sort_order: NotRequired["aws_sdk_marketplace_catalog.types.sort_order.SortOrder"]
    """<p>The sorting order. Can be <code>ASCENDING</code> or <code>DESCENDING</code>. The default value is <code>DESCENDING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductSort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_marketplace_catalog.types.data_product_sort_by

        out["SortBy"] = (
            aws_sdk_marketplace_catalog.types.data_product_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_marketplace_catalog.types.sort_order

        out["SortOrder"] = aws_sdk_marketplace_catalog.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> DataProductSort:
    out: DataProductSort = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_marketplace_catalog.types.data_product_sort_by

        out["sort_by"] = (
            aws_sdk_marketplace_catalog.types.data_product_sort_by.deserialize_json(
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
