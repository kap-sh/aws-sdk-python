"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicDateRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.topic_range_filter_constant


class TopicDateRangeFilter(TypedDict, closed=True):
    inclusive: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the date range filter should include the boundary values. If set to true, the filter includes the start and end dates. If set to false, the filter excludes them.</p>"""
    constant: NotRequired[
        "capo_quicksight.types.topic_range_filter_constant.TopicRangeFilterConstant"
    ]
    """<p>The constant used in a date range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicDateRangeFilter) -> dict:
    out: dict = {}
    out["Inclusive"] = value.get("inclusive", False)
    if "constant" in value:
        import capo_quicksight.types.topic_range_filter_constant

        out["Constant"] = (
            capo_quicksight.types.topic_range_filter_constant.serialize_json(
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
        import capo_quicksight.types.topic_range_filter_constant

        out["constant"] = (
            capo_quicksight.types.topic_range_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    return out
