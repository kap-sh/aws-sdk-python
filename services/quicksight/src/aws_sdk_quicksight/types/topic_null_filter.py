"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNullFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.null_filter_type
    import aws_sdk_quicksight.types.topic_singular_filter_constant


class TopicNullFilter(TypedDict):
    null_filter_type: NotRequired[
        "aws_sdk_quicksight.types.null_filter_type.NullFilterType"
    ]
    """<p>The type of the null filter. Valid values for this type are <code>NULLS_ONLY</code>, <code>NON_NULLS_ONLY</code>, and <code>ALL_VALUES</code>.</p>"""
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_singular_filter_constant.TopicSingularFilterConstant"
    ]
    inverse: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates if the filter is inverse.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNullFilter) -> dict:
    out: dict = {}
    if "null_filter_type" in value:
        import aws_sdk_quicksight.types.null_filter_type

        out["NullFilterType"] = (
            aws_sdk_quicksight.types.null_filter_type.serialize_json(
                value["null_filter_type"]
            )
        )
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_singular_filter_constant

        out["Constant"] = (
            aws_sdk_quicksight.types.topic_singular_filter_constant.serialize_json(
                value["constant"]
            )
        )
    out["Inverse"] = value.get("inverse", False)
    return out


def deserialize_json(data: dict) -> TopicNullFilter:
    out: TopicNullFilter = {}  # type: ignore[typeddict-item]
    if "NullFilterType" in data:
        import aws_sdk_quicksight.types.null_filter_type

        out["null_filter_type"] = (
            aws_sdk_quicksight.types.null_filter_type.deserialize_json(
                data["NullFilterType"]
            )
        )
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_singular_filter_constant

        out["constant"] = (
            aws_sdk_quicksight.types.topic_singular_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if "Inverse" in data:
        out["inverse"] = data["Inverse"]
    else:
        out["inverse"] = False
    return out
