"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicDateRangeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.topic_range_filter_constant


class TopicDateRangeFilter(TypedDict):
    inclusive: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the date range filter should include the boundary values. If set to true, the filter includes the start and end dates. If set to false, the filter excludes them.</p>"""
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_range_filter_constant.TopicRangeFilterConstant"
    ]
    """<p>The constant used in a date range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicDateRangeFilter) -> dict:
    out: dict = {}
    out["Inclusive"] = value.get("inclusive", False)
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_range_filter_constant

        out["Constant"] = (
            aws_sdk_quicksight.types.topic_range_filter_constant.serialize_json(
                value["constant"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicDateRangeFilter:
    out: TopicDateRangeFilter = {}  # type: ignore[typeddict-item]
    if "Inclusive" in data:
        out["inclusive"] = data["Inclusive"]
    else:
        out["inclusive"] = False
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_range_filter_constant

        out["constant"] = (
            aws_sdk_quicksight.types.topic_range_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    return out
