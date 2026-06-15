"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryMetadataFilterExpression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_left_expression
    import aws_sdk_bedrock_agentcore.types.memory_record_operator_type
    import aws_sdk_bedrock_agentcore.types.memory_record_right_expression


class MemoryMetadataFilterExpression(TypedDict):
    left: "aws_sdk_bedrock_agentcore.types.memory_record_left_expression.MemoryRecordLeftExpression"
    """<p>The metadata key to evaluate.</p>"""
    operator: "aws_sdk_bedrock_agentcore.types.memory_record_operator_type.MemoryRecordOperatorType"
    """<p>The relationship between the metadata key and value to match when applying the metadata filter.</p>"""
    right: NotRequired[
        "aws_sdk_bedrock_agentcore.types.memory_record_right_expression.MemoryRecordRightExpression"
    ]
    """<p>The value to compare against. Required for all operators except EXISTS and NOT_EXISTS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryMetadataFilterExpression) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_record_left_expression

    out["left"] = (
        aws_sdk_bedrock_agentcore.types.memory_record_left_expression.serialize_json(
            value["left"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.memory_record_operator_type

    out["operator"] = (
        aws_sdk_bedrock_agentcore.types.memory_record_operator_type.serialize_json(
            value["operator"]
        )
    )
    if "right" in value:
        import aws_sdk_bedrock_agentcore.types.memory_record_right_expression

        out["right"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_right_expression.serialize_json(
                value["right"]
            )
        )
    return out


def deserialize_json(data: dict) -> MemoryMetadataFilterExpression:
    out: MemoryMetadataFilterExpression = {}  # type: ignore[typeddict-item]
    if "left" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_left_expression

        out["left"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_left_expression.deserialize_json(
                data["left"]
            )
        )
    else:
        raise DeserializationError("MemoryMetadataFilterExpression.left required")
    if "operator" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_operator_type

        out["operator"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_operator_type.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("MemoryMetadataFilterExpression.operator required")
    if "right" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_right_expression

        out["right"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_right_expression.deserialize_json(
                data["right"]
            )
        )
    return out
