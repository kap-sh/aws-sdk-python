"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductTitleFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_title_filter_value_list
    import aws_sdk_marketplace_catalog.types.machine_learning_product_title_string


class MachineLearningProductTitleFilter(TypedDict):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.machine_learning_product_title_filter_value_list.MachineLearningProductTitleFilterValueList"
    ]
    """<p>A list of product titles to filter by. The operation returns machine learning products with titles that exactly match the values in this list.</p>"""
    wild_card_value: NotRequired[
        "aws_sdk_marketplace_catalog.types.machine_learning_product_title_string.MachineLearningProductTitleString"
    ]
    """<p>A wildcard value to filter product titles. The operation returns machine learning products with titles that match this wildcard pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductTitleFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_title_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_title_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    if "wild_card_value" in value:
        out["WildCardValue"] = value["wild_card_value"]
    return out


def deserialize_json(data: dict) -> MachineLearningProductTitleFilter:
    out: MachineLearningProductTitleFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_title_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_title_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    if "WildCardValue" in data:
        out["wild_card_value"] = data["WildCardValue"]
    return out
