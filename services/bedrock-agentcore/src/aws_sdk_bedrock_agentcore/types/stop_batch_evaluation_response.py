"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopBatchEvaluationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_arn
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_description
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_status


class StopBatchEvaluationResponse(TypedDict):
    batch_evaluation_id: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    )
    """<p>The unique identifier of the stopped batch evaluation.</p>"""
    batch_evaluation_arn: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_arn.BatchEvaluationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the stopped batch evaluation.</p>"""
    status: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_status.BatchEvaluationStatus"
    )
    """<p>The status of the batch evaluation after the stop request.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
    ]
    """<p>The description of the batch evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBatchEvaluationResponse) -> dict:
    out: dict = {}
    out["batchEvaluationId"] = value["batch_evaluation_id"]
    out["batchEvaluationArn"] = value["batch_evaluation_arn"]
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.batch_evaluation_status.serialize_json(
            value["status"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StopBatchEvaluationResponse:
    out: StopBatchEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "batchEvaluationId" in data:
        out["batch_evaluation_id"] = data["batchEvaluationId"]
    else:
        raise DeserializationError(
            "StopBatchEvaluationResponse.batch_evaluation_id required"
        )
    if "batchEvaluationArn" in data:
        out["batch_evaluation_arn"] = data["batchEvaluationArn"]
    else:
        raise DeserializationError(
            "StopBatchEvaluationResponse.batch_evaluation_arn required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.batch_evaluation_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.batch_evaluation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StopBatchEvaluationResponse.status required")
    if "description" in data:
        out["description"] = data["description"]
    return out
