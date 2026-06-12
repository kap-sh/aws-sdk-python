"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#MachineLearningProductVisibilityFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_filter_value_list


class MachineLearningProductVisibilityFilter(TypedDict):
    value_list: NotRequired[
        "aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_filter_value_list.MachineLearningProductVisibilityFilterValueList"
    ]
    """<p>A list of visibility values to filter by. The operation returns machine learning products with visibility status that match the values in this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningProductVisibilityFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_filter_value_list

        out["ValueList"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> MachineLearningProductVisibilityFilter:
    out: MachineLearningProductVisibilityFilter = {}  # type: ignore[typeddict-item]
    if "ValueList" in data:
        import aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_filter_value_list

        out["value_list"] = (
            aws_sdk_marketplace_catalog.types.machine_learning_product_visibility_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
