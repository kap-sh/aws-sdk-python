"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericRangeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration
    import aws_sdk_quicksight.types.filter_null_option
    import aws_sdk_quicksight.types.numeric_filter_select_all_options
    import aws_sdk_quicksight.types.numeric_range_filter_value
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class NumericRangeFilter(TypedDict):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    include_minimum: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the minimum value in the filter value range should be included in the filtered results.</p>"""
    include_maximum: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the maximum value in the filter value range should be included in the filtered results.</p>"""
    range_minimum: NotRequired[
        "aws_sdk_quicksight.types.numeric_range_filter_value.NumericRangeFilterValue"
    ]
    """<p>The minimum value for the filter value range.</p>"""
    range_maximum: NotRequired[
        "aws_sdk_quicksight.types.numeric_range_filter_value.NumericRangeFilterValue"
    ]
    """<p>The maximum value for the filter value range.</p>"""
    select_all_options: NotRequired[
        "aws_sdk_quicksight.types.numeric_filter_select_all_options.NumericFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function of the filter.</p>"""
    null_option: "aws_sdk_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericRangeFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "include_minimum" in value:
        out["IncludeMinimum"] = value["include_minimum"]
    if "include_maximum" in value:
        out["IncludeMaximum"] = value["include_maximum"]
    if "range_minimum" in value:
        import aws_sdk_quicksight.types.numeric_range_filter_value

        out["RangeMinimum"] = (
            aws_sdk_quicksight.types.numeric_range_filter_value.serialize_json(
                value["range_minimum"]
            )
        )
    if "range_maximum" in value:
        import aws_sdk_quicksight.types.numeric_range_filter_value

        out["RangeMaximum"] = (
            aws_sdk_quicksight.types.numeric_range_filter_value.serialize_json(
                value["range_maximum"]
            )
        )
    if "select_all_options" in value:
        import aws_sdk_quicksight.types.numeric_filter_select_all_options

        out["SelectAllOptions"] = (
            aws_sdk_quicksight.types.numeric_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    import aws_sdk_quicksight.types.filter_null_option

    out["NullOption"] = aws_sdk_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    if "default_filter_control_configuration" in value:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericRangeFilter:
    out: NumericRangeFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("NumericRangeFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NumericRangeFilter.column required")
    if "IncludeMinimum" in data:
        out["include_minimum"] = data["IncludeMinimum"]
    if "IncludeMaximum" in data:
        out["include_maximum"] = data["IncludeMaximum"]
    if "RangeMinimum" in data:
        import aws_sdk_quicksight.types.numeric_range_filter_value

        out["range_minimum"] = (
            aws_sdk_quicksight.types.numeric_range_filter_value.deserialize_json(
                data["RangeMinimum"]
            )
        )
    if "RangeMaximum" in data:
        import aws_sdk_quicksight.types.numeric_range_filter_value

        out["range_maximum"] = (
            aws_sdk_quicksight.types.numeric_range_filter_value.deserialize_json(
                data["RangeMaximum"]
            )
        )
    if "SelectAllOptions" in data:
        import aws_sdk_quicksight.types.numeric_filter_select_all_options

        out["select_all_options"] = (
            aws_sdk_quicksight.types.numeric_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if "NullOption" in data:
        import aws_sdk_quicksight.types.filter_null_option

        out["null_option"] = (
            aws_sdk_quicksight.types.filter_null_option.deserialize_json(
                data["NullOption"]
            )
        )
    else:
        raise DeserializationError("NumericRangeFilter.null_option required")
    if "DefaultFilterControlConfiguration" in data:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
