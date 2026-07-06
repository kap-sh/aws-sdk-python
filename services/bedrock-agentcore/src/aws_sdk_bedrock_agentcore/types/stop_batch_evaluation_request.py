"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StopBatchEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id


class StopBatchEvaluationRequest(TypedDict, closed=True):
    batch_evaluation_id: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    )
    """<p>The unique identifier of the batch evaluation to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopBatchEvaluationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopBatchEvaluationRequest:
    out: StopBatchEvaluationRequest = {}  # type: ignore[typeddict-item]
    return out
