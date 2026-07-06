"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventMetadataFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.left_expression
    import aws_sdk_bedrock_agentcore.types.operator_type
    import aws_sdk_bedrock_agentcore.types.right_expression


class EventMetadataFilterExpression(TypedDict, closed=True):
    left: "aws_sdk_bedrock_agentcore.types.left_expression.LeftExpression"
    """<p>Left operand of the event metadata filter expression.</p>"""
    operator: "aws_sdk_bedrock_agentcore.types.operator_type.OperatorType"
    """<p>Operator applied to the event metadata filter expression.</p>"""
    right: NotRequired[
        "aws_sdk_bedrock_agentcore.types.right_expression.RightExpression"
    ]
    """<p>Right operand of the event metadata filter expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventMetadataFilterExpression) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.left_expression

    out["left"] = aws_sdk_bedrock_agentcore.types.left_expression.serialize_json(
        value["left"]
    )
    import aws_sdk_bedrock_agentcore.types.operator_type

    out["operator"] = aws_sdk_bedrock_agentcore.types.operator_type.serialize_json(
        value["operator"]
    )
    if "right" in value:
        import aws_sdk_bedrock_agentcore.types.right_expression

        out["right"] = aws_sdk_bedrock_agentcore.types.right_expression.serialize_json(
            value["right"]
        )
    return out


def deserialize_json(data: dict) -> EventMetadataFilterExpression:
    out: EventMetadataFilterExpression = {}  # type: ignore[typeddict-item]
    if "left" in data:
        import aws_sdk_bedrock_agentcore.types.left_expression

        out["left"] = aws_sdk_bedrock_agentcore.types.left_expression.deserialize_json(
            data["left"]
        )
    else:
        raise DeserializationError("EventMetadataFilterExpression.left required")
    if "operator" in data:
        import aws_sdk_bedrock_agentcore.types.operator_type

        out["operator"] = (
            aws_sdk_bedrock_agentcore.types.operator_type.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("EventMetadataFilterExpression.operator required")
    if "right" in data:
        import aws_sdk_bedrock_agentcore.types.right_expression

        out["right"] = (
            aws_sdk_bedrock_agentcore.types.right_expression.deserialize_json(
                data["right"]
            )
        )
    return out
