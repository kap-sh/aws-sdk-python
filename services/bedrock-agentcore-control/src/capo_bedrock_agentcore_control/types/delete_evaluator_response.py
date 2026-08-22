"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteEvaluatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_arn
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_status


class DeleteEvaluatorResponse(TypedDict, closed=True):
    evaluator_arn: "capo_bedrock_agentcore_control.types.evaluator_arn.EvaluatorArn"
    """<p> The Amazon Resource Name (ARN) of the deleted evaluator. </p>"""
    evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the deleted evaluator. </p>"""
    status: "capo_bedrock_agentcore_control.types.evaluator_status.EvaluatorStatus"
    """<p> The status of the evaluator deletion operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEvaluatorResponse) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    out["evaluatorId"] = value["evaluator_id"]
    import capo_bedrock_agentcore_control.types.evaluator_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.evaluator_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteEvaluatorResponse:
    out: DeleteEvaluatorResponse = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorArn") is not None:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        raise DeserializationError("DeleteEvaluatorResponse.evaluator_arn required")
    if data.get("evaluatorId") is not None:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        raise DeserializationError("DeleteEvaluatorResponse.evaluator_id required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.evaluator_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteEvaluatorResponse.status required")
    return out
