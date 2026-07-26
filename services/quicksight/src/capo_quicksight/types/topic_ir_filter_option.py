"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agg_function_param_map
    import capo_quicksight.types.agg_type
    import capo_quicksight.types.aggregation_partition_by_list
    import capo_quicksight.types.anchor
    import capo_quicksight.types.boolean
    import capo_quicksight.types.filter_agg_metrics_list
    import capo_quicksight.types.filter_class
    import capo_quicksight.types.identifier
    import capo_quicksight.types.null_filter_option
    import capo_quicksight.types.time_granularity
    import capo_quicksight.types.topic_constant_value
    import capo_quicksight.types.topic_ir_filter_function
    import capo_quicksight.types.topic_ir_filter_type
    import capo_quicksight.types.topic_sort_direction


class TopicIRFilterOption(TypedDict, closed=True):
    filter_type: NotRequired[
        "capo_quicksight.types.topic_ir_filter_type.TopicIRFilterType"
    ]
    """<p>The filter type for the <code>TopicIRFilterOption</code>.</p>"""
    filter_class: NotRequired["capo_quicksight.types.filter_class.FilterClass"]
    """<p>The filter class for the <code>TopicIRFilterOption</code>.</p>"""
    operand_field: NotRequired["capo_quicksight.types.identifier.Identifier"]
    """<p>The operand field for the <code>TopicIRFilterOption</code>.</p>"""
    function: NotRequired[
        "capo_quicksight.types.topic_ir_filter_function.TopicIRFilterFunction"
    ]
    """<p>The function for the <code>TopicIRFilterOption</code>.</p>"""
    constant: NotRequired[
        "capo_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The constant for the <code>TopicIRFilterOption</code>.</p>"""
    inverse: "capo_quicksight.types.boolean.Boolean"
    """<p>The inverse for the <code>TopicIRFilterOption</code>.</p>"""
    null_filter: NotRequired[
        "capo_quicksight.types.null_filter_option.NullFilterOption"
    ]
    """<p>The null filter for the <code>TopicIRFilterOption</code>.</p>"""
    aggregation: NotRequired["capo_quicksight.types.agg_type.AggType"]
    """<p>The aggregation for the <code>TopicIRFilterOption</code>.</p>"""
    aggregation_function_parameters: NotRequired[
        "capo_quicksight.types.agg_function_param_map.AggFunctionParamMap"
    ]
    """<p>The aggregation function parameters for the <code>TopicIRFilterOption</code>.</p>"""
    aggregation_partition_by: NotRequired[
        "capo_quicksight.types.aggregation_partition_by_list.AggregationPartitionByList"
    ]
    """<p>The <code>AggregationPartitionBy</code> for the <code>TopicIRFilterOption</code>.</p>"""
    range: NotRequired["capo_quicksight.types.topic_constant_value.TopicConstantValue"]
    """<p>The range for the <code>TopicIRFilterOption</code>.</p>"""
    inclusive: "capo_quicksight.types.boolean.Boolean"
    """<p>The inclusive for the <code>TopicIRFilterOption</code>.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity for the <code>TopicIRFilterOption</code>.</p>"""
    last_next_offset: NotRequired[
        "capo_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The last next offset for the <code>TopicIRFilterOption</code>.</p>"""
    agg_metrics: NotRequired[
        "capo_quicksight.types.filter_agg_metrics_list.FilterAggMetricsList"
    ]
    """<p>The agg metrics for the <code>TopicIRFilterOption</code>.</p>"""
    top_bottom_limit: NotRequired[
        "capo_quicksight.types.topic_constant_value.TopicConstantValue"
    ]
    """<p>The <code>TopBottomLimit</code> for the <code>TopicIRFilterOption</code>.</p>"""
    sort_direction: NotRequired[
        "capo_quicksight.types.topic_sort_direction.TopicSortDirection"
    ]
    """<p>The sort direction for the <code>TopicIRFilterOption</code>.</p>"""
    anchor: NotRequired["capo_quicksight.types.anchor.Anchor"]
    """<p>The anchor for the <code>TopicIRFilterOption</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRFilterOption) -> dict:
    out: dict = {}
    if "filter_type" in value:
        import capo_quicksight.types.topic_ir_filter_type

        out["FilterType"] = capo_quicksight.types.topic_ir_filter_type.serialize_json(
            value["filter_type"]
        )
    if "filter_class" in value:
        import capo_quicksight.types.filter_class

        out["FilterClass"] = capo_quicksight.types.filter_class.serialize_json(
            value["filter_class"]
        )
    if "operand_field" in value:
        import capo_quicksight.types.identifier

        out["OperandField"] = capo_quicksight.types.identifier.serialize_json(
            value["operand_field"]
        )
    if "function" in value:
        import capo_quicksight.types.topic_ir_filter_function

        out["Function"] = capo_quicksight.types.topic_ir_filter_function.serialize_json(
            value["function"]
        )
    if "constant" in value:
        import capo_quicksight.types.topic_constant_value

        out["Constant"] = capo_quicksight.types.topic_constant_value.serialize_json(
            value["constant"]
        )
    out["Inverse"] = value.get("inverse", False)
    if "null_filter" in value:
        import capo_quicksight.types.null_filter_option

        out["NullFilter"] = capo_quicksight.types.null_filter_option.serialize_json(
            value["null_filter"]
        )
    if "aggregation" in value:
        import capo_quicksight.types.agg_type

        out["Aggregation"] = capo_quicksight.types.agg_type.serialize_json(
            value["aggregation"]
        )
    if "aggregation_function_parameters" in value:
        import capo_quicksight.types.agg_function_param_map

        out["AggregationFunctionParameters"] = (
            capo_quicksight.types.agg_function_param_map.serialize_json(
                value["aggregation_function_parameters"]
            )
        )
    if "aggregation_partition_by" in value:
        import capo_quicksight.types.aggregation_partition_by_list

        out["AggregationPartitionBy"] = (
            capo_quicksight.types.aggregation_partition_by_list.serialize_json(
                value["aggregation_partition_by"]
            )
        )
    if "range" in value:
        import capo_quicksight.types.topic_constant_value

        out["Range"] = capo_quicksight.types.topic_constant_value.serialize_json(
            value["range"]
        )
    out["Inclusive"] = value.get("inclusive", False)
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    if "last_next_offset" in value:
        import capo_quicksight.types.topic_constant_value

        out["LastNextOffset"] = (
            capo_quicksight.types.topic_constant_value.serialize_json(
                value["last_next_offset"]
            )
        )
    if "agg_metrics" in value:
        import capo_quicksight.types.filter_agg_metrics_list

        out["AggMetrics"] = (
            capo_quicksight.types.filter_agg_metrics_list.serialize_json(
                value["agg_metrics"]
            )
        )
    if "top_bottom_limit" in value:
        import capo_quicksight.types.topic_constant_value

        out["TopBottomLimit"] = (
            capo_quicksight.types.topic_constant_value.serialize_json(
                value["top_bottom_limit"]
            )
        )
    if "sort_direction" in value:
        import capo_quicksight.types.topic_sort_direction

        out["SortDirection"] = (
            capo_quicksight.types.topic_sort_direction.serialize_json(
                value["sort_direction"]
            )
        )
    if "anchor" in value:
        import capo_quicksight.types.anchor

        out["Anchor"] = capo_quicksight.types.anchor.serialize_json(value["anchor"])
    return out


def deserialize_json(data: dict) -> TopicIRFilterOption:
    out: TopicIRFilterOption = {}  # type: ignore[typeddict-item]
    if "FilterType" in data:
        import capo_quicksight.types.topic_ir_filter_type

        out["filter_type"] = (
            capo_quicksight.types.topic_ir_filter_type.deserialize_json(
                data["FilterType"]
            )
        )
    if "FilterClass" in data:
        import capo_quicksight.types.filter_class

        out["filter_class"] = capo_quicksight.types.filter_class.deserialize_json(
            data["FilterClass"]
        )
    if "OperandField" in data:
        import capo_quicksight.types.identifier

        out["operand_field"] = capo_quicksight.types.identifier.deserialize_json(
            data["OperandField"]
        )
    if "Function" in data:
        import capo_quicksight.types.topic_ir_filter_function

        out["function"] = (
            capo_quicksight.types.topic_ir_filter_function.deserialize_json(
                data["Function"]
            )
        )
    if "Constant" in data:
        import capo_quicksight.types.topic_constant_value

        out["constant"] = capo_quicksight.types.topic_constant_value.deserialize_json(
            data["Constant"]
        )
    if "Inverse" in data:
        out["inverse"] = data["Inverse"]
    else:
        out["inverse"] = False
    if "NullFilter" in data:
        import capo_quicksight.types.null_filter_option

        out["null_filter"] = capo_quicksight.types.null_filter_option.deserialize_json(
            data["NullFilter"]
        )
    if "Aggregation" in data:
        import capo_quicksight.types.agg_type

        out["aggregation"] = capo_quicksight.types.agg_type.deserialize_json(
            data["Aggregation"]
        )
    if "AggregationFunctionParameters" in data:
        import capo_quicksight.types.agg_function_param_map

        out["aggregation_function_parameters"] = (
            capo_quicksight.types.agg_function_param_map.deserialize_json(
                data["AggregationFunctionParameters"]
            )
        )
    if "AggregationPartitionBy" in data:
        import capo_quicksight.types.aggregation_partition_by_list

        out["aggregation_partition_by"] = (
            capo_quicksight.types.aggregation_partition_by_list.deserialize_json(
                data["AggregationPartitionBy"]
            )
        )
    if "Range" in data:
        import capo_quicksight.types.topic_constant_value

        out["range"] = capo_quicksight.types.topic_constant_value.deserialize_json(
            data["Range"]
        )
    if "Inclusive" in data:
        out["inclusive"] = data["Inclusive"]
    else:
        out["inclusive"] = False
    if "TimeGranularity" in data:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "LastNextOffset" in data:
        import capo_quicksight.types.topic_constant_value

        out["last_next_offset"] = (
            capo_quicksight.types.topic_constant_value.deserialize_json(
                data["LastNextOffset"]
            )
        )
    if "AggMetrics" in data:
        import capo_quicksight.types.filter_agg_metrics_list

        out["agg_metrics"] = (
            capo_quicksight.types.filter_agg_metrics_list.deserialize_json(
                data["AggMetrics"]
            )
        )
    if "TopBottomLimit" in data:
        import capo_quicksight.types.topic_constant_value

        out["top_bottom_limit"] = (
            capo_quicksight.types.topic_constant_value.deserialize_json(
                data["TopBottomLimit"]
            )
        )
    if "SortDirection" in data:
        import capo_quicksight.types.topic_sort_direction

        out["sort_direction"] = (
            capo_quicksight.types.topic_sort_direction.deserialize_json(
                data["SortDirection"]
            )
        )
    if "Anchor" in data:
        import capo_quicksight.types.anchor

        out["anchor"] = capo_quicksight.types.anchor.deserialize_json(data["Anchor"])
    return out
