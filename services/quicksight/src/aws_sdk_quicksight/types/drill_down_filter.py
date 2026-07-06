"""Generated from Smithy shape ``com.amazonaws.quicksight#DrillDownFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_drill_down_filter
    import aws_sdk_quicksight.types.numeric_equality_drill_down_filter
    import aws_sdk_quicksight.types.time_range_drill_down_filter


class DrillDownFilter(TypedDict, closed=True):
    numeric_equality_filter: NotRequired[
        "aws_sdk_quicksight.types.numeric_equality_drill_down_filter.NumericEqualityDrillDownFilter"
    ]
    """<p>The numeric equality type drill down filter. This filter is used for number type columns.</p>"""
    category_filter: NotRequired[
        "aws_sdk_quicksight.types.category_drill_down_filter.CategoryDrillDownFilter"
    ]
    """<p>The category type drill down filter. This filter is used for string type columns.</p>"""
    time_range_filter: NotRequired[
        "aws_sdk_quicksight.types.time_range_drill_down_filter.TimeRangeDrillDownFilter"
    ]
    """<p>The time range drill down filter. This filter is used for date time columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DrillDownFilter) -> dict:
    out: dict = {}
    if "numeric_equality_filter" in value:
        import aws_sdk_quicksight.types.numeric_equality_drill_down_filter

        out["NumericEqualityFilter"] = (
            aws_sdk_quicksight.types.numeric_equality_drill_down_filter.serialize_json(
                value["numeric_equality_filter"]
            )
        )
    if "category_filter" in value:
        import aws_sdk_quicksight.types.category_drill_down_filter

        out["CategoryFilter"] = (
            aws_sdk_quicksight.types.category_drill_down_filter.serialize_json(
                value["category_filter"]
            )
        )
    if "time_range_filter" in value:
        import aws_sdk_quicksight.types.time_range_drill_down_filter

        out["TimeRangeFilter"] = (
            aws_sdk_quicksight.types.time_range_drill_down_filter.serialize_json(
                value["time_range_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> DrillDownFilter:
    out: DrillDownFilter = {}  # type: ignore[typeddict-item]
    if "NumericEqualityFilter" in data:
        import aws_sdk_quicksight.types.numeric_equality_drill_down_filter

        out["numeric_equality_filter"] = (
            aws_sdk_quicksight.types.numeric_equality_drill_down_filter.deserialize_json(
                data["NumericEqualityFilter"]
            )
        )
    if "CategoryFilter" in data:
        import aws_sdk_quicksight.types.category_drill_down_filter

        out["category_filter"] = (
            aws_sdk_quicksight.types.category_drill_down_filter.deserialize_json(
                data["CategoryFilter"]
            )
        )
    if "TimeRangeFilter" in data:
        import aws_sdk_quicksight.types.time_range_drill_down_filter

        out["time_range_filter"] = (
            aws_sdk_quicksight.types.time_range_drill_down_filter.deserialize_json(
                data["TimeRangeFilter"]
            )
        )
    return out
