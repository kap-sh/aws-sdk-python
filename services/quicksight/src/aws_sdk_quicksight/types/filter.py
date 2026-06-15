"""Generated from Smithy shape ``com.amazonaws.quicksight#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_filter
    import aws_sdk_quicksight.types.nested_filter
    import aws_sdk_quicksight.types.numeric_equality_filter
    import aws_sdk_quicksight.types.numeric_range_filter
    import aws_sdk_quicksight.types.relative_dates_filter
    import aws_sdk_quicksight.types.time_equality_filter
    import aws_sdk_quicksight.types.time_range_filter
    import aws_sdk_quicksight.types.top_bottom_filter


class Filter(TypedDict):
    category_filter: NotRequired[
        "aws_sdk_quicksight.types.category_filter.CategoryFilter"
    ]
    r"""<p>A <code>CategoryFilter</code> filters text values.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/add-a-text-filter-data-prep.html\">Adding text filters</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""
    numeric_range_filter: NotRequired[
        "aws_sdk_quicksight.types.numeric_range_filter.NumericRangeFilter"
    ]
    """<p>A <code>NumericRangeFilter</code> filters numeric values that are either inside or outside a given numeric range.</p>"""
    numeric_equality_filter: NotRequired[
        "aws_sdk_quicksight.types.numeric_equality_filter.NumericEqualityFilter"
    ]
    """<p>A <code>NumericEqualityFilter</code> filters numeric values that equal or do not equal a given numeric value.</p>"""
    time_equality_filter: NotRequired[
        "aws_sdk_quicksight.types.time_equality_filter.TimeEqualityFilter"
    ]
    """<p>A <code>TimeEqualityFilter</code> filters date-time values that equal or do not equal a given date/time value.</p>"""
    time_range_filter: NotRequired[
        "aws_sdk_quicksight.types.time_range_filter.TimeRangeFilter"
    ]
    """<p>A <code>TimeRangeFilter</code> filters date-time values that are either inside or outside a given date/time range.</p>"""
    relative_dates_filter: NotRequired[
        "aws_sdk_quicksight.types.relative_dates_filter.RelativeDatesFilter"
    ]
    """<p>A <code>RelativeDatesFilter</code> filters date values that are relative to a given date.</p>"""
    top_bottom_filter: NotRequired[
        "aws_sdk_quicksight.types.top_bottom_filter.TopBottomFilter"
    ]
    """<p>A <code>TopBottomFilter</code> filters data to the top or bottom values for a given column.</p>"""
    nested_filter: NotRequired["aws_sdk_quicksight.types.nested_filter.NestedFilter"]
    """<p>A <code>NestedFilter</code> filters data with a subset of data that is defined by the nested inner filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "category_filter" in value:
        import aws_sdk_quicksight.types.category_filter

        out["CategoryFilter"] = aws_sdk_quicksight.types.category_filter.serialize_json(
            value["category_filter"]
        )
    if "numeric_range_filter" in value:
        import aws_sdk_quicksight.types.numeric_range_filter

        out["NumericRangeFilter"] = (
            aws_sdk_quicksight.types.numeric_range_filter.serialize_json(
                value["numeric_range_filter"]
            )
        )
    if "numeric_equality_filter" in value:
        import aws_sdk_quicksight.types.numeric_equality_filter

        out["NumericEqualityFilter"] = (
            aws_sdk_quicksight.types.numeric_equality_filter.serialize_json(
                value["numeric_equality_filter"]
            )
        )
    if "time_equality_filter" in value:
        import aws_sdk_quicksight.types.time_equality_filter

        out["TimeEqualityFilter"] = (
            aws_sdk_quicksight.types.time_equality_filter.serialize_json(
                value["time_equality_filter"]
            )
        )
    if "time_range_filter" in value:
        import aws_sdk_quicksight.types.time_range_filter

        out["TimeRangeFilter"] = (
            aws_sdk_quicksight.types.time_range_filter.serialize_json(
                value["time_range_filter"]
            )
        )
    if "relative_dates_filter" in value:
        import aws_sdk_quicksight.types.relative_dates_filter

        out["RelativeDatesFilter"] = (
            aws_sdk_quicksight.types.relative_dates_filter.serialize_json(
                value["relative_dates_filter"]
            )
        )
    if "top_bottom_filter" in value:
        import aws_sdk_quicksight.types.top_bottom_filter

        out["TopBottomFilter"] = (
            aws_sdk_quicksight.types.top_bottom_filter.serialize_json(
                value["top_bottom_filter"]
            )
        )
    if "nested_filter" in value:
        import aws_sdk_quicksight.types.nested_filter

        out["NestedFilter"] = aws_sdk_quicksight.types.nested_filter.serialize_json(
            value["nested_filter"]
        )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "CategoryFilter" in data:
        import aws_sdk_quicksight.types.category_filter

        out["category_filter"] = (
            aws_sdk_quicksight.types.category_filter.deserialize_json(
                data["CategoryFilter"]
            )
        )
    if "NumericRangeFilter" in data:
        import aws_sdk_quicksight.types.numeric_range_filter

        out["numeric_range_filter"] = (
            aws_sdk_quicksight.types.numeric_range_filter.deserialize_json(
                data["NumericRangeFilter"]
            )
        )
    if "NumericEqualityFilter" in data:
        import aws_sdk_quicksight.types.numeric_equality_filter

        out["numeric_equality_filter"] = (
            aws_sdk_quicksight.types.numeric_equality_filter.deserialize_json(
                data["NumericEqualityFilter"]
            )
        )
    if "TimeEqualityFilter" in data:
        import aws_sdk_quicksight.types.time_equality_filter

        out["time_equality_filter"] = (
            aws_sdk_quicksight.types.time_equality_filter.deserialize_json(
                data["TimeEqualityFilter"]
            )
        )
    if "TimeRangeFilter" in data:
        import aws_sdk_quicksight.types.time_range_filter

        out["time_range_filter"] = (
            aws_sdk_quicksight.types.time_range_filter.deserialize_json(
                data["TimeRangeFilter"]
            )
        )
    if "RelativeDatesFilter" in data:
        import aws_sdk_quicksight.types.relative_dates_filter

        out["relative_dates_filter"] = (
            aws_sdk_quicksight.types.relative_dates_filter.deserialize_json(
                data["RelativeDatesFilter"]
            )
        )
    if "TopBottomFilter" in data:
        import aws_sdk_quicksight.types.top_bottom_filter

        out["top_bottom_filter"] = (
            aws_sdk_quicksight.types.top_bottom_filter.deserialize_json(
                data["TopBottomFilter"]
            )
        )
    if "NestedFilter" in data:
        import aws_sdk_quicksight.types.nested_filter

        out["nested_filter"] = aws_sdk_quicksight.types.nested_filter.deserialize_json(
            data["NestedFilter"]
        )
    return out
