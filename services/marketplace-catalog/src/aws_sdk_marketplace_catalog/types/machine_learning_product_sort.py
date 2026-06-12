"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductSort``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_sort_by
    import aws_sdk_marketplace_catalog.types.sort_order


class MachineLearningProductSort(TypedDict):
    sort_by: NotRequired[
        "aws_sdk_marketplace_catalog.types.machine_learning_product_sort_by.MachineLearningProductSortBy"
    ]
    """<p>The field to sort by. Valid values: <code>EntityId</code>, <code>LastModifiedDate</code>, <code>ProductTitle</code>, and <code>Visibility</code>.</p>"""
    sort_order: NotRequired["aws_sdk_marketplace_catalog.types.sort_order.SortOrder"]
    """<p>The sort order. Valid values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductSort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_sort_by

        out["SortBy"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_marketplace_catalog.types.sort_order

        out["SortOrder"] = aws_sdk_marketplace_catalog.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> MachineLearningProductSort:
    out: MachineLearningProductSort = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_sort_by

        out["sort_by"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_sort_by.deserialize_json(
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
