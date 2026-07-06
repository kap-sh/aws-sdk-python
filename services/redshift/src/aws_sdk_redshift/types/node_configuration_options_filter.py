"""Generated from Smithy shape ``com.amazonaws.redshift#NodeConfigurationOptionsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.node_configuration_options_filter_name
    import aws_sdk_redshift.types.operator_type
    import aws_sdk_redshift.types.value_string_list


class NodeConfigurationOptionsFilter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_redshift.types.node_configuration_options_filter_name.NodeConfigurationOptionsFilterName"
    ]
    """<p>The name of the element to filter.</p>"""
    operator: NotRequired["aws_sdk_redshift.types.operator_type.OperatorType"]
    """<p>The filter operator. If filter Name is NodeType only the 'in' operator is supported. Provide one value to evaluate for 'eq', 'lt', 'le', 'gt', and 'ge'. Provide two values to evaluate for 'between'. Provide a list of values for 'in'.</p>"""
    values: NotRequired["aws_sdk_redshift.types.value_string_list.ValueStringList"]
    """<p>List of values. Compare Name using Operator to Values. If filter Name is NumberOfNodes, then values can range from 0 to 200. If filter Name is EstimatedDiskUtilizationPercent, then values can range from 0 to 100. For example, filter NumberOfNodes (name) GT (operator) 3 (values).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeConfigurationOptionsFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        import aws_sdk_redshift.types.node_configuration_options_filter_name

        aws_sdk_redshift.types.node_configuration_options_filter_name.serialize_query(
            value["name"], pairs, f"{prefix}.Name"
        )
    if "operator" in value:
        import aws_sdk_redshift.types.operator_type

        aws_sdk_redshift.types.operator_type.serialize_query(
            value["operator"], pairs, f"{prefix}.Operator"
        )
    if "values" in value:
        import aws_sdk_redshift.types.value_string_list

        aws_sdk_redshift.types.value_string_list.serialize_query(
            value["values"], pairs, f"{prefix}.Value"
        )


def deserialize_query(el: Element) -> NodeConfigurationOptionsFilter:
    out: NodeConfigurationOptionsFilter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import aws_sdk_redshift.types.node_configuration_options_filter_name

        out["name"] = (
            aws_sdk_redshift.types.node_configuration_options_filter_name.deserialize_query(
                child_name
            )
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import aws_sdk_redshift.types.operator_type

        out["operator"] = aws_sdk_redshift.types.operator_type.deserialize_query(
            child_operator
        )
    child_values = el.find("Value")
    if child_values is not None:
        import aws_sdk_redshift.types.value_string_list

        out["values"] = aws_sdk_redshift.types.value_string_list.deserialize_query(
            child_values
        )
    return out
