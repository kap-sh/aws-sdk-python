"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DuplicateConditionExpressionFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_condition_expression
    import capo_bedrock_agent.types.flow_node_name


class DuplicateConditionExpressionFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the duplicate condition expressions.</p>"""
    expression: (
        "capo_bedrock_agent.types.flow_condition_expression.FlowConditionExpression"
    )
    """<p>The duplicated condition expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DuplicateConditionExpressionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> DuplicateConditionExpressionFlowValidationDetails:
    out: DuplicateConditionExpressionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "DuplicateConditionExpressionFlowValidationDetails.node required"
        )
    if "expression" in data:
        out["expression"] = data["expression"]
    else:
        raise DeserializationError(
            "DuplicateConditionExpressionFlowValidationDetails.expression required"
        )
    return out
