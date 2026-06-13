"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetBatchEvaluationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id

class GetBatchEvaluationRequest(TypedDict):
    batch_evaluation_id: "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    """<p>The unique identifier of the batch evaluation to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetBatchEvaluationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBatchEvaluationRequest:
    out: GetBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
    return out