"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericEqualityFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.default_filter_control_configuration
    import aws_sdk_quicksight.types.double
    import aws_sdk_quicksight.types.filter_null_option
    import aws_sdk_quicksight.types.numeric_equality_match_operator
    import aws_sdk_quicksight.types.numeric_filter_select_all_options
    import aws_sdk_quicksight.types.parameter_name
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class NumericEqualityFilter(TypedDict):
    filter_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.double.Double"]
    """<p>The input value.</p>"""
    select_all_options: NotRequired[
        "aws_sdk_quicksight.types.numeric_filter_select_all_options.NumericFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    match_operator: "aws_sdk_quicksight.types.numeric_equality_match_operator.NumericEqualityMatchOperator"
    """<p>The match operator that is used to determine if a filter should be applied.</p>"""
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function of the filter.</p>"""
    parameter_name: NotRequired["aws_sdk_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p>"""
    null_option: "aws_sdk_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    default_filter_control_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericEqualityFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "value" in value:
        out["Value"] = value["value"]
    if "select_all_options" in value:
        import aws_sdk_quicksight.types.numeric_filter_select_all_options

        out["SelectAllOptions"] = (
            aws_sdk_quicksight.types.numeric_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    import aws_sdk_quicksight.types.numeric_equality_match_operator

    out["MatchOperator"] = (
        aws_sdk_quicksight.types.numeric_equality_match_operator.serialize_json(
            value["match_operator"]
        )
    )
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
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


def deserialize_json(data: dict) -> NumericEqualityFilter:
    out: NumericEqualityFilter = {}  # type: ignore[typeddict-item]
    if "FilterId" in data:
        out["filter_id"] = data["FilterId"]
    else:
        raise DeserializationError("NumericEqualityFilter.filter_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NumericEqualityFilter.column required")
    if "Value" in data:
        out["value"] = data["Value"]
    if "SelectAllOptions" in data:
        import aws_sdk_quicksight.types.numeric_filter_select_all_options

        out["select_all_options"] = (
            aws_sdk_quicksight.types.numeric_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if "MatchOperator" in data:
        import aws_sdk_quicksight.types.numeric_equality_match_operator

        out["match_operator"] = (
            aws_sdk_quicksight.types.numeric_equality_match_operator.deserialize_json(
                data["MatchOperator"]
            )
        )
    else:
        raise DeserializationError("NumericEqualityFilter.match_operator required")
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "NullOption" in data:
        import aws_sdk_quicksight.types.filter_null_option

        out["null_option"] = (
            aws_sdk_quicksight.types.filter_null_option.deserialize_json(
                data["NullOption"]
            )
        )
    else:
        raise DeserializationError("NumericEqualityFilter.null_option required")
    if "DefaultFilterControlConfiguration" in data:
        import aws_sdk_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            aws_sdk_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
