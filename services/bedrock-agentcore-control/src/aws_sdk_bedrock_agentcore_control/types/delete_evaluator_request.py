"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteEvaluatorRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.evaluator_id

class DeleteEvaluatorRequest(TypedDict):
    evaluator_id: "aws_sdk_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator to delete. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteEvaluatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEvaluatorRequest:
    out: DeleteEvaluatorRequest = {}  # type: ignore[typeddict-item]
    return out