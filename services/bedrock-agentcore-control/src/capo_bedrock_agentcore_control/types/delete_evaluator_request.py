"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteEvaluatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_id


class DeleteEvaluatorRequest(TypedDict, closed=True):
    evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEvaluatorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEvaluatorRequest:
    out: DeleteEvaluatorRequest = {}  # type: ignore[typeddict-item]
    return out
