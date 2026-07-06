"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agg_function_param_map
    import aws_sdk_quicksight.types.agg_type
    import aws_sdk_quicksight.types.aggregation_partition_by_list
    import aws_sdk_quicksight.types.anchor
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.filter_agg_metrics_list
    import aws_sdk_quicksight.types.filter_class
    import aws_sdk_quicksight.types.identifier
    import aws_sdk_quicksight.types.null_filter_option
    import aws_sdk_quicksight.types.time_granularity
    import aws_sdk_quicksight.types.topic_constant_value
    import aws_sdk_quicksight.types.topic_ir_filter_function
    import aws_sdk_quicksight.types.topic_ir_filter_type
    import aws_sdk_quicksight.types.topic_sort_direction


class TopicIRFilterOption(TypedDict, closed=True):
    filter_type: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_filter_type.TopicIRFilterType"
    ]
    """<p>The filter type for the <code>TopicIRFilterOption</code>.</p>"""
    filter_class: NotRequired["aws_sdk_quicksight.types.filter_class.FilterClass"]
    """<p>The filter class for the <code>TopicIRFilterOption</code>.</p>"""
    operand_field: NotRequired["aws_sdk_quicksight.types.identifier.Identifier"]
    """<p>The operand field for the <code>TopicIRFilterOption</code>.</p>"""
    function: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_filter_function.TopicIRFilterFunction"
    ]
    """<p>The function for the <code>TopicIRFilterOption</code>.</p>"""
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The constant for the <code>TopicIRFilterOption</code>.</p>"""
    inverse: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The inverse for the <code>TopicIRFilterOption</code>.</p>"""
    null_filter: NotRequired[
        "aws_sdk_quicksight.types.null_filter_option.NullFilterOption"
    ]
    """<p>The null filter for the <code>TopicIRFilterOption</code>.</p>"""
    aggregation: NotRequired["aws_sdk_quicksight.types.agg_type.AggType"]
    """<p>The aggregation for the <code>TopicIRFilterOption</code>.</p>"""
    aggregation_function_parameters: NotRequired[
        "aws_sdk_quicksight.types.agg_function_param_map.AggFunctionParamMap"
    ]
    """<p>The aggregation function parameters for the <code>TopicIRFilterOption</code>.</p>"""
    aggregation_partition_by: NotRequired[
        "aws_sdk_quicksight.types.aggregation_partition_by_list.AggregationPartitionByList"
    ]
    """<p>The <code>AggregationPartitionBy</code> for the <code>TopicIRFilterOption</code>.</p>"""
    range: NotRequired[
        "aws_sdk_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The range for the <code>TopicIRFilterOption</code>.</p>"""
    inclusive: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>The inclusive for the <code>TopicIRFilterOption</code>.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity for the <code>TopicIRFilterOption</code>.</p>"""
    last_next_offset: NotRequired[
        "aws_sdk_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The last next offset for the <code>TopicIRFilterOption</code>.</p>"""
    agg_metrics: NotRequired[
        "aws_sdk_quicksight.types.filter_agg_metrics_list.FilterAggMetricsList"
    ]
    """<p>The agg metrics for the <code>TopicIRFilterOption</code>.</p>"""
    top_bottom_limit: NotRequired[
        "aws_sdk_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The <code>TopBottomLimit</code> for the <code>TopicIRFilterOption</code>.</p>"""
    sort_direction: NotRequired[
        "aws_sdk_quicksight.types.topic_sort_direction.TopicSortDirection"
    ]
    """<p>The sort direction for the <code>TopicIRFilterOption</code>.</p>"""
    anchor: NotRequired["aws_sdk_quicksight.types.anchor.Anchor"]
    """<p>The anchor for the <code>TopicIRFilterOption</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRFilterOption) -> dict:
    out: dict = {}
    if "filter_type" in value:
        import aws_sdk_quicksight.types.topic_ir_filter_type

        out["FilterType"] = (
            aws_sdk_quicksight.types.topic_ir_filter_type.serialize_json(
                value["filter_type"]
            )
        )
    if "filter_class" in value:
        import aws_sdk_quicksight.types.filter_class

        out["FilterClass"] = aws_sdk_quicksight.types.filter_class.serialize_json(
            value["filter_class"]
        )
    if "operand_field" in value:
        import aws_sdk_quicksight.types.identifier

        out["OperandField"] = aws_sdk_quicksight.types.identifier.serialize_json(
            value["operand_field"]
        )
    if "function" in value:
        import aws_sdk_quicksight.types.topic_ir_filter_function

        out["Function"] = (
            aws_sdk_quicksight.types.topic_ir_filter_function.serialize_json(
                value["function"]
            )
        )
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_constant_value

        out["Constant"] = aws_sdk_quicksight.types.topic_constant_value.serialize_json(
            value["constant"]
        )
    out["Inverse"] = value.get("inverse", False)
    if "null_filter" in value:
        import aws_sdk_quicksight.types.null_filter_option

        out["NullFilter"] = aws_sdk_quicksight.types.null_filter_option.serialize_json(
            value["null_filter"]
        )
    if "aggregation" in value:
        import aws_sdk_quicksight.types.agg_type

        out["Aggregation"] = aws_sdk_quicksight.types.agg_type.serialize_json(
            value["aggregation"]
        )
    if "aggregation_function_parameters" in value:
        import aws_sdk_quicksight.types.agg_function_param_map

        out["AggregationFunctionParameters"] = (
            aws_sdk_quicksight.types.agg_function_param_map.serialize_json(
                value["aggregation_function_parameters"]
            )
        )
    if "aggregation_partition_by" in value:
        import aws_sdk_quicksight.types.aggregation_partition_by_list

        out["AggregationPartitionBy"] = (
            aws_sdk_quicksight.types.aggregation_partition_by_list.serialize_json(
                value["aggregation_partition_by"]
            )
        )
    if "range" in value:
        import aws_sdk_quicksight.types.topic_constant_value

        out["Range"] = aws_sdk_quicksight.types.topic_constant_value.serialize_json(
            value["range"]
        )
    out["Inclusive"] = value.get("inclusive", False)
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "last_next_offset" in value:
        import aws_sdk_quicksight.types.topic_constant_value

        out["LastNextOffset"] = (
            aws_sdk_quicksight.types.topic_constant_value.serialize_json(
                value["last_next_offset"]
            )
        )
    if "agg_metrics" in value:
        import aws_sdk_quicksight.types.filter_agg_metrics_list

        out["AggMetrics"] = (
            aws_sdk_quicksight.types.filter_agg_metrics_list.serialize_json(
                value["agg_metrics"]
            )
        )
    if "top_bottom_limit" in value:
        import aws_sdk_quicksight.types.topic_constant_value

        out["TopBottomLimit"] = (
            aws_sdk_quicksight.types.topic_constant_value.serialize_json(
                value["top_bottom_limit"]
            )
        )
    if "sort_direction" in value:
        import aws_sdk_quicksight.types.topic_sort_direction

        out["SortDirection"] = (
            aws_sdk_quicksight.types.topic_sort_direction.serialize_json(
                value["sort_direction"]
            )
        )
    if "anchor" in value:
        import aws_sdk_quicksight.types.anchor

        out["Anchor"] = aws_sdk_quicksight.types.anchor.serialize_json(value["anchor"])
    return out


def deserialize_json(data: dict) -> TopicIRFilterOption:
    out: TopicIRFilterOption = {}  # type: ignore[typeddict-item]
    if "FilterType" in data:
        import aws_sdk_quicksight.types.topic_ir_filter_type

        out["filter_type"] = (
            aws_sdk_quicksight.types.topic_ir_filter_type.deserialize_json(
                data["FilterType"]
            )
        )
    if "FilterClass" in data:
        import aws_sdk_quicksight.types.filter_class

        out["filter_class"] = aws_sdk_quicksight.types.filter_class.deserialize_json(
            data["FilterClass"]
        )
    if "OperandField" in data:
        import aws_sdk_quicksight.types.identifier

        out["operand_field"] = aws_sdk_quicksight.types.identifier.deserialize_json(
            data["OperandField"]
        )
    if "Function" in data:
        import aws_sdk_quicksight.types.topic_ir_filter_function

        out["function"] = (
            aws_sdk_quicksight.types.topic_ir_filter_function.deserialize_json(
                data["Function"]
            )
        )
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_constant_value

        out["constant"] = (
            aws_sdk_quicksight.types.topic_constant_value.deserialize_json(
                data["Constant"]
            )
        )
    if "Inverse" in data:
        out["inverse"] = data["Inverse"]
    else:
        out["inverse"] = False
    if "NullFilter" in data:
        import aws_sdk_quicksight.types.null_filter_option

        out["null_filter"] = (
            aws_sdk_quicksight.types.null_filter_option.deserialize_json(
                data["NullFilter"]
            )
        )
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.agg_type

        out["aggregation"] = aws_sdk_quicksight.types.agg_type.deserialize_json(
            data["Aggregation"]
        )
    if "AggregationFunctionParameters" in data:
        import aws_sdk_quicksight.types.agg_function_param_map

        out["aggregation_function_parameters"] = (
            aws_sdk_quicksight.types.agg_function_param_map.deserialize_json(
                data["AggregationFunctionParameters"]
            )
        )
    if "AggregationPartitionBy" in data:
        import aws_sdk_quicksight.types.aggregation_partition_by_list

        out["aggregation_partition_by"] = (
            aws_sdk_quicksight.types.aggregation_partition_by_list.deserialize_json(
                data["AggregationPartitionBy"]
            )
        )
    if "Range" in data:
        import aws_sdk_quicksight.types.topic_constant_value

        out["range"] = aws_sdk_quicksight.types.topic_constant_value.deserialize_json(
            data["Range"]
        )
    if "Inclusive" in data:
        out["inclusive"] = data["Inclusive"]
    else:
        out["inclusive"] = False
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "LastNextOffset" in data:
        import aws_sdk_quicksight.types.topic_constant_value

        out["last_next_offset"] = (
            aws_sdk_quicksight.types.topic_constant_value.deserialize_json(
                data["LastNextOffset"]
            )
        )
    if "AggMetrics" in data:
        import aws_sdk_quicksight.types.filter_agg_metrics_list

        out["agg_metrics"] = (
            aws_sdk_quicksight.types.filter_agg_metrics_list.deserialize_json(
                data["AggMetrics"]
            )
        )
    if "TopBottomLimit" in data:
        import aws_sdk_quicksight.types.topic_constant_value

        out["top_bottom_limit"] = (
            aws_sdk_quicksight.types.topic_constant_value.deserialize_json(
                data["TopBottomLimit"]
            )
        )
    if "SortDirection" in data:
        import aws_sdk_quicksight.types.topic_sort_direction

        out["sort_direction"] = (
            aws_sdk_quicksight.types.topic_sort_direction.deserialize_json(
                data["SortDirection"]
            )
        )
    if "Anchor" in data:
        import aws_sdk_quicksight.types.anchor

        out["anchor"] = aws_sdk_quicksight.types.anchor.deserialize_json(data["Anchor"])
    return out
