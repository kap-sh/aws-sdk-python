"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_input_category
    import aws_sdk_bedrock_agent.types.flow_node_input_expression
    import aws_sdk_bedrock_agent.types.flow_node_input_name
    import aws_sdk_bedrock_agent.types.flow_node_io_data_type


class FlowNodeInput(TypedDict):
    name: "aws_sdk_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>Specifies a name for the input that you can reference.</p>"""
    type: "aws_sdk_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType"
    """<p>Specifies the data type of the input. If the input doesn't match this type at runtime, a validation error will be thrown.</p>"""
    expression: (
        "aws_sdk_bedrock_agent.types.flow_node_input_expression.FlowNodeInputExpression"
    )
    r"""<p>An expression that formats the input for the node. For an explanation of how to create expressions, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html\">Expressions in Prompt flows in Amazon Bedrock</a>.</p>"""
    category: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_node_input_category.FlowNodeInputCategory"
    ]
    """<p>Specifies how input data flows between iterations in a DoWhile loop.</p> <ul> <li> <p> <code>LoopCondition</code> - Controls whether the loop continues by evaluating condition expressions against the input data. Use this category to define the condition that determines if the loop should continue. </p> </li> <li> <p> <code>ReturnValueToLoopStart</code> - Defines data to pass back to the start of the loop's next iteration. Use this category for variables that you want to update for each loop iteration.</p> </li> <li> <p> <code>ExitLoop</code> - Defines the value that's available once the loop ends. Use this category to expose loop results to nodes outside the loop.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent.types.flow_node_io_data_type

    out["type"] = aws_sdk_bedrock_agent.types.flow_node_io_data_type.serialize_json(
        value["type"]
    )
    out["expression"] = value["expression"]
    if "category" in value:
        import aws_sdk_bedrock_agent.types.flow_node_input_category

        out["category"] = (
            aws_sdk_bedrock_agent.types.flow_node_input_category.serialize_json(
                value["category"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowNodeInput:
    out: FlowNodeInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowNodeInput.name required")
    if "type" in data:
        import aws_sdk_bedrock_agent.types.flow_node_io_data_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.flow_node_io_data_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("FlowNodeInput.type required")
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError("FlowNodeInput.expression required")
    if "category" in data:
        import aws_sdk_bedrock_agent.types.flow_node_input_category

        out["category"] = (
            aws_sdk_bedrock_agent.types.flow_node_input_category.deserialize_json(
                data["category"]
            )
        )
    return out
