"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductVisibilityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.data_product_visibility_filter_value_list


class DataProductVisibilityFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.data_product_visibility_filter_value_list.DataProductVisibilityFilterValueList"
    ]
    """<p>A string array of unique visibility values to be filtered on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductVisibilityFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.data_product_visibility_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.data_product_visibility_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataProductVisibilityFilter:
    out: DataProductVisibilityFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.data_product_visibility_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.data_product_visibility_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
