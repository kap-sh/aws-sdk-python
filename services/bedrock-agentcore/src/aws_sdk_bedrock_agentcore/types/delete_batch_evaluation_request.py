"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteBatchEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id


class DeleteBatchEvaluationRequest(TypedDict, closed=True):
    batch_evaluation_id: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    )
    """<p>The unique identifier of the batch evaluation to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBatchEvaluationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBatchEvaluationRequest:
    out: DeleteBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
    return out
