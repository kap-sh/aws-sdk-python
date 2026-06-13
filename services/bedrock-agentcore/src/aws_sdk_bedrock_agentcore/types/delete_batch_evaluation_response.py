"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteBatchEvaluationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_arn
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_status

class DeleteBatchEvaluationResponse(TypedDict):
    batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    """<p>The unique identifier of the deleted batch evaluation.</p>"""
    batch_evaluation_arn: "aws_sdk_bedrock_agentcore.types.batch_evaluation_arn.BatchEvaluationArn"
    """<p>The Amazon Resource Name (ARN) of the deleted batch evaluation.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.batch_evaluation_status.BatchEvaluationStatus"
    """<p>The status of the batch evaluation deletion operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteBatchEvaluationResponse) -> dict:
    out: dict = {}
    out["batchEvaluationId"] = value["batch_evaluation_id"]
    out["batchEvaluationArn"] = value["batch_evaluation_arn"]
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_status
    out["status"] = aws_sdk_bedrock_agentcore.types.batch_evaluation_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteBatchEvaluationResponse:
    out: DeleteBatchEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "batchEvaluationId" in data:
        out["batch_evaluation_id"] = data["batchEvaluationId"]
    else:
        raise DeserializationError("DeleteBatchEvaluationResponse.batch_evaluation_id required")
    if "batchEvaluationArn" in data:
        out["batch_evaluation_arn"] = data["batchEvaluationArn"]
    else:
        raise DeserializationError("DeleteBatchEvaluationResponse.batch_evaluation_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.batch_evaluation_status
        out["status"] = aws_sdk_bedrock_agentcore.types.batch_evaluation_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteBatchEvaluationResponse.status required")
    return out