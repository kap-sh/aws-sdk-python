"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicCategoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.category_filter_function
    import aws_sdk_quicksight.types.category_filter_type
    import aws_sdk_quicksight.types.topic_category_filter_constant


class TopicCategoryFilter(TypedDict, closed=True):
    category_filter_function: NotRequired[
        "aws_sdk_quicksight.types.category_filter_function.CategoryFilterFunction"
    ]
    """<p>The category filter function. Valid values for this structure are <code>EXACT</code> and <code>CONTAINS</code>.</p>"""
    category_filter_type: NotRequired[
        "aws_sdk_quicksight.types.category_filter_type.CategoryFilterType"
    ]
    """<p>The category filter type. This element is used to specify whether a filter is a simple category filter or an inverse category filter.</p>"""
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_category_filter_constant.TopicCategoryFilterConstant"
    ]
    """<p>The constant used in a category filter.</p>"""
    inverse: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates if the filter is inverse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicCategoryFilter) -> dict:
    out: dict = {}
    if "category_filter_function" in value:
        import aws_sdk_quicksight.types.category_filter_function

        out["CategoryFilterFunction"] = (
            aws_sdk_quicksight.types.category_filter_function.serialize_json(
                value["category_filter_function"]
            )
        )
    if "category_filter_type" in value:
        import aws_sdk_quicksight.types.category_filter_type

        out["CategoryFilterType"] = (
            aws_sdk_quicksight.types.category_filter_type.serialize_json(
                value["category_filter_type"]
            )
        )
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_category_filter_constant

        out["Constant"] = (
            aws_sdk_quicksight.types.topic_category_filter_constant.serialize_json(
                value["constant"]
            )
        )
    out["Inverse"] = value.get("inverse", False)
    return out


def deserialize_json(data: dict) -> TopicCategoryFilter:
    out: TopicCategoryFilter = {}  # type: ignore[typeddict-item]
    if "CategoryFilterFunction" in data:
        import aws_sdk_quicksight.types.category_filter_function

        out["category_filter_function"] = (
            aws_sdk_quicksight.types.category_filter_function.deserialize_json(
                data["CategoryFilterFunction"]
            )
        )
    if "CategoryFilterType" in data:
        import aws_sdk_quicksight.types.category_filter_type

        out["category_filter_type"] = (
            aws_sdk_quicksight.types.category_filter_type.deserialize_json(
                data["CategoryFilterType"]
            )
        )
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_category_filter_constant

        out["constant"] = (
            aws_sdk_quicksight.types.topic_category_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if "Inverse" in data:
        out["inverse"] = data["Inverse"]
    else:
        out["inverse"] = False
    return out
