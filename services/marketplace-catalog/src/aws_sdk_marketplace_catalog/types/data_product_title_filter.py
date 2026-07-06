"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductTitleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.data_product_title_filter_value_list
    import aws_sdk_marketplace_catalog.types.data_product_title_string


class DataProductTitleFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.data_product_title_filter_value_list.DataProductTitleFilterValueList"
    ]
    """<p>A string array of unique product title values to be filtered on.</p>"""
    wild_card_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.data_product_title_string.DataProductTitleString"
    ]
    """<p>A string that will be the <code>wildCard</code> input for product tile filter. It matches the provided value as a substring in the actual value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductTitleFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.data_product_title_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.data_product_title_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    if "wild_card_value" in value:
        out["WildCardValue"] = value["wild_card_value"]
    return out


def deserialize_json(data: dict) -> DataProductTitleFilter:
    out: DataProductTitleFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.data_product_title_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.data_product_title_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    if "WildCardValue" in data:
        out["wild_card_value"] = data["WildCardValue"]
    return out
