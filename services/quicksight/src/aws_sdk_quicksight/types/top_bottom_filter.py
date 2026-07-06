"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_sort_configuration_list
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration
    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.time_granularity


class TopBottomFilter(TypedDict, closed=True):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    limit: NotRequired["aws_sdk_quicksight.types.integer.Integer"]
    """<p>The number of items to include in the top bottom filter results.</p>"""
    aggregation_sort_configurations: "aws_sdk_quicksight.types.aggregation_sort_configuration_list.AggregationSortConfigurationList"
    """<p>The aggregation and sort configuration of the top bottom filter.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    parameter_name: NotRequired["aws_sdk_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p>"""
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "limit" in value:
        out["Limit"] = value["limit"]
    import aws_sdk_quicksight.types.aggregation_sort_configuration_list

    out["AggregationSortConfigurations"] = (
        aws_sdk_quicksight.types.aggregation_sort_configuration_list.serialize_json(
            value["aggregation_sort_configurations"]
        )
    )
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "default_filter_control_configuration" in value:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopBottomFilter:
    out: TopBottomFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("TopBottomFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("TopBottomFilter.column required")
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "AggregationSortConfigurations" in data:
        import aws_sdk_quicksight.types.aggregation_sort_configuration_list

        out["aggregation_sort_configurations"] = (
            aws_sdk_quicksight.types.aggregation_sort_configuration_list.deserialize_json(
                data["AggregationSortConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "TopBottomFilter.aggregation_sort_configurations required"
        )
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "DefaultFilterControlConfiguration" in data:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
