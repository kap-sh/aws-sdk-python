"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeRangeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration
    import aws_sdk_quicksight.types.exclude_period_configuration
    import aws_sdk_quicksight.types.filter_null_option
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.time_granularity
    import aws_sdk_quicksight.types.time_range_filter_value


class TimeRangeFilter(TypedDict):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    include_minimum: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the minimum value in the filter value range should be included in the filtered results.</p>"""
    include_maximum: NotRequired["aws_sdk_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the maximum value in the filter value range should be included in the filtered results.</p>"""
    range_minimum_value: NotRequired[
        "aws_sdk_quicksight.types.time_range_filter_value.TimeRangeFilterValue"
    ]
    """<p>The minimum value for the filter value range.</p>"""
    range_maximum_value: NotRequired[
        "aws_sdk_quicksight.types.time_range_filter_value.TimeRangeFilterValue"
    ]
    """<p>The maximum value for the filter value range.</p>"""
    null_option: "aws_sdk_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    exclude_period_configuration: NotRequired[
        "aws_sdk_quicksight.types.exclude_period_configuration.ExcludePeriodConfiguration"
    ]
    """<p>The exclude period of the time range filter.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeFilter) -> dict:
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
    if "range_minimum_value" in value:
        import aws_sdk_quicksight.types.time_range_filter_value

        out["RangeMinimumValue"] = (
            aws_sdk_quicksight.types.time_range_filter_value.serialize_json(
                value["range_minimum_value"]
            )
        )
    if "range_maximum_value" in value:
        import aws_sdk_quicksight.types.time_range_filter_value

        out["RangeMaximumValue"] = (
            aws_sdk_quicksight.types.time_range_filter_value.serialize_json(
                value["range_maximum_value"]
            )
        )
    import aws_sdk_quicksight.types.filter_null_option

    out["NullOption"] = aws_sdk_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    if "exclude_period_configuration" in value:
        import aws_sdk_quicksight.types.exclude_period_configuration

        out["ExcludePeriodConfiguration"] = (
            aws_sdk_quicksight.types.exclude_period_configuration.serialize_json(
                value["exclude_period_configuration"]
            )
        )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "default_filter_control_configuration" in value:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimeRangeFilter:
    out: TimeRangeFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("TimeRangeFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("TimeRangeFilter.column required")
    if "IncludeMinimum" in data:
        out["include_minimum"] = data["IncludeMinimum"]
    if "IncludeMaximum" in data:
        out["include_maximum"] = data["IncludeMaximum"]
    if "RangeMinimumValue" in data:
        import aws_sdk_quicksight.types.time_range_filter_value

        out["range_minimum_value"] = (
            aws_sdk_quicksight.types.time_range_filter_value.deserialize_json(
                data["RangeMinimumValue"]
            )
        )
    if "RangeMaximumValue" in data:
        import aws_sdk_quicksight.types.time_range_filter_value

        out["range_maximum_value"] = (
            aws_sdk_quicksight.types.time_range_filter_value.deserialize_json(
                data["RangeMaximumValue"]
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
        raise DeserializationError("TimeRangeFilter.null_option required")
    if "ExcludePeriodConfiguration" in data:
        import aws_sdk_quicksight.types.exclude_period_configuration

        out["exclude_period_configuration"] = (
            aws_sdk_quicksight.types.exclude_period_configuration.deserialize_json(
                data["ExcludePeriodConfiguration"]
            )
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "DefaultFilterControlConfiguration" in data:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
