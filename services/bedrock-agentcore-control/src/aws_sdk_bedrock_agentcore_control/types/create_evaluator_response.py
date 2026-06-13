"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateEvaluatorResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_evaluator_arn
    import aws_sdk_bedrock_agentcore_control.types.evaluator_id
    import aws_sdk_bedrock_agentcore_control.types.evaluator_status
    import datetime

class CreateEvaluatorResponse(TypedDict):
    evaluator_arn: "aws_sdk_bedrock_agentcore_control.types.custom_evaluator_arn.CustomEvaluatorArn"
    """<p> The Amazon Resource Name (ARN) of the created evaluator. </p>"""
    evaluator_id: "aws_sdk_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the created evaluator. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the evaluator was created. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.evaluator_status.EvaluatorStatus"
    """<p> The status of the evaluator creation operation. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluatorResponse) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    out["evaluatorId"] = value["evaluator_id"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.evaluator_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.evaluator_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateEvaluatorResponse:
    out: CreateEvaluatorResponse = {}  # type: ignore[typeddict-item]
    if "evaluatorArn" in data:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        raise DeserializationError("CreateEvaluatorResponse.evaluator_arn required")
    if "evaluatorId" in data:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        raise DeserializationError("CreateEvaluatorResponse.evaluator_id required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateEvaluatorResponse.created_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.evaluator_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateEvaluatorResponse.status required")
    return out