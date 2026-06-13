"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agg_function
    import aws_sdk_quicksight.types.calculated_field_reference_list
    import aws_sdk_quicksight.types.display_format
    import aws_sdk_quicksight.types.display_format_options
    import aws_sdk_quicksight.types.expression
    import aws_sdk_quicksight.types.identifier
    import aws_sdk_quicksight.types.named_entity_ref
    import aws_sdk_quicksight.types.operand_list
    import aws_sdk_quicksight.types.topic_ir_comparison_method


class TopicIRMetric(TypedDict):
    metric_id: NotRequired["aws_sdk_quicksight.types.identifier.Identifier"]
    """<p>The metric ID for the <code>TopicIRMetric</code>.</p>"""
    function: NotRequired["aws_sdk_quicksight.types.agg_function.AggFunction"]
    """<p>The function for the <code>TopicIRMetric</code>.</p>"""
    operands: NotRequired["aws_sdk_quicksight.types.operand_list.OperandList"]
    """<p>The operands for the <code>TopicIRMetric</code>.</p>"""
    comparison_method: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_comparison_method.TopicIRComparisonMethod"
    ]
    """<p>The comparison method for the <code>TopicIRMetric</code>.</p>"""
    expression: NotRequired["aws_sdk_quicksight.types.expression.Expression"]
    """<p>The expression for the <code>TopicIRMetric</code>.</p>"""
    calculated_field_references: NotRequired[
        "aws_sdk_quicksight.types.calculated_field_reference_list.CalculatedFieldReferenceList"
    ]
    """<p>The calculated field references for the <code>TopicIRMetric</code>.</p>"""
    display_format: NotRequired["aws_sdk_quicksight.types.display_format.DisplayFormat"]
    """<p>The display format for the <code>TopicIRMetric</code>.</p>"""
    display_format_options: NotRequired[
        "aws_sdk_quicksight.types.display_format_options.DisplayFormatOptions"
    ]
    named_entity: NotRequired[
        "aws_sdk_quicksight.types.named_entity_ref.NamedEntityRef"
    ]
    """<p>The named entity for the <code>TopicIRMetric</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRMetric) -> dict:
    out: dict = {}
    if "metric_id" in value:
        import aws_sdk_quicksight.types.identifier

        out["MetricId"] = aws_sdk_quicksight.types.identifier.serialize_json(
            value["metric_id"]
        )
    if "function" in value:
        import aws_sdk_quicksight.types.agg_function

        out["Function"] = aws_sdk_quicksight.types.agg_function.serialize_json(
            value["function"]
        )
    if "operands" in value:
        import aws_sdk_quicksight.types.operand_list

        out["Operands"] = aws_sdk_quicksight.types.operand_list.serialize_json(
            value["operands"]
        )
    if "comparison_method" in value:
        import aws_sdk_quicksight.types.topic_ir_comparison_method

        out["ComparisonMethod"] = (
            aws_sdk_quicksight.types.topic_ir_comparison_method.serialize_json(
                value["comparison_method"]
            )
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "calculated_field_references" in value:
        import aws_sdk_quicksight.types.calculated_field_reference_list

        out["CalculatedFieldReferences"] = (
            aws_sdk_quicksight.types.calculated_field_reference_list.serialize_json(
                value["calculated_field_references"]
            )
        )
    if "display_format" in value:
        import aws_sdk_quicksight.types.display_format

        out["DisplayFormat"] = aws_sdk_quicksight.types.display_format.serialize_json(
            value["display_format"]
        )
    if "display_format_options" in value:
        import aws_sdk_quicksight.types.display_format_options

        out["DisplayFormatOptions"] = (
            aws_sdk_quicksight.types.display_format_options.serialize_json(
                value["display_format_options"]
            )
        )
    if "named_entity" in value:
        import aws_sdk_quicksight.types.named_entity_ref

        out["NamedEntity"] = aws_sdk_quicksight.types.named_entity_ref.serialize_json(
            value["named_entity"]
        )
    return out


def deserialize_json(data: dict) -> TopicIRMetric:
    out: TopicIRMetric = {}  # type: ignore[typeddict-item]
    if "MetricId" in data:
        import aws_sdk_quicksight.types.identifier

        out["metric_id"] = aws_sdk_quicksight.types.identifier.deserialize_json(
            data["MetricId"]
        )
    if "Function" in data:
        import aws_sdk_quicksight.types.agg_function

        out["function"] = aws_sdk_quicksight.types.agg_function.deserialize_json(
            data["Function"]
        )
    if "Operands" in data:
        import aws_sdk_quicksight.types.operand_list

        out["operands"] = aws_sdk_quicksight.types.operand_list.deserialize_json(
            data["Operands"]
        )
    if "ComparisonMethod" in data:
        import aws_sdk_quicksight.types.topic_ir_comparison_method

        out["comparison_method"] = (
            aws_sdk_quicksight.types.topic_ir_comparison_method.deserialize_json(
                data["ComparisonMethod"]
            )
        )
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "CalculatedFieldReferences" in data:
        import aws_sdk_quicksight.types.calculated_field_reference_list

        out["calculated_field_references"] = (
            aws_sdk_quicksight.types.calculated_field_reference_list.deserialize_json(
                data["CalculatedFieldReferences"]
            )
        )
    if "DisplayFormat" in data:
        import aws_sdk_quicksight.types.display_format

        out["display_format"] = (
            aws_sdk_quicksight.types.display_format.deserialize_json(
                data["DisplayFormat"]
            )
        )
    if "DisplayFormatOptions" in data:
        import aws_sdk_quicksight.types.display_format_options

        out["display_format_options"] = (
            aws_sdk_quicksight.types.display_format_options.deserialize_json(
                data["DisplayFormatOptions"]
            )
        )
    if "NamedEntity" in data:
        import aws_sdk_quicksight.types.named_entity_ref

        out["named_entity"] = (
            aws_sdk_quicksight.types.named_entity_ref.deserialize_json(
                data["NamedEntity"]
            )
        )
    return out
