"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeEqualityFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.rolling_date_configuration
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.time_granularity
    import aws_sdk_quicksight.types.timestamp


class TimeEqualityFilter(TypedDict):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The value of a <code>TimeEquality</code> filter.</p> <p>This field is mutually exclusive to <code>RollingDate</code> and <code>ParameterName</code>.</p>"""
    parameter_name: NotRequired["aws_sdk_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p> <p>This field is mutually exclusive to <code>Value</code> and <code>RollingDate</code>.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    rolling_date: NotRequired[
        "aws_sdk_quicksight.types.rolling_date_configuration.RollingDateConfiguration"
    ]
    """<p>The rolling date input for the <code>TimeEquality</code> filter.</p> <p>This field is mutually exclusive to <code>Value</code> and <code>ParameterName</code>.</p>"""
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeEqualityFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "value" in value:
        import aws_sdk_quicksight.types.timestamp

        out["Value"] = aws_sdk_quicksight.types.timestamp.serialize_json(value["value"])
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "rolling_date" in value:
        import aws_sdk_quicksight.types.rolling_date_configuration

        out["RollingDate"] = (
            aws_sdk_quicksight.types.rolling_date_configuration.serialize_json(
                value["rolling_date"]
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


def deserialize_json(data: dict) -> TimeEqualityFilter:
    out: TimeEqualityFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("TimeEqualityFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("TimeEqualityFilter.column required")
    if "Value" in data:
        import aws_sdk_quicksight.types.timestamp

        out["value"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["Value"]
        )
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "RollingDate" in data:
        import aws_sdk_quicksight.types.rolling_date_configuration

        out["rolling_date"] = (
            aws_sdk_quicksight.types.rolling_date_configuration.deserialize_json(
                data["RollingDate"]
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
