"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateEvaluatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.custom_evaluator_arn
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_status


class CreateEvaluatorResponse(TypedDict, closed=True):
    evaluator_arn: (
        "capo_bedrock_agentcore_control.types.custom_evaluator_arn.CustomEvaluatorArn"
    )
    """<p> The Amazon Resource Name (ARN) of the created evaluator. </p>"""
    evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the created evaluator. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the evaluator was created. </p>"""
    status: "capo_bedrock_agentcore_control.types.evaluator_status.EvaluatorStatus"
    """<p> The status of the evaluator creation operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluatorResponse) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    out["evaluatorId"] = value["evaluator_id"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.evaluator_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.evaluator_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateEvaluatorResponse:
    out: CreateEvaluatorResponse = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorArn") is not None:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        raise DeserializationError("CreateEvaluatorResponse.evaluator_arn required")
    if data.get("evaluatorId") is not None:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        raise DeserializationError("CreateEvaluatorResponse.evaluator_id required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateEvaluatorResponse.created_at required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.evaluator_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateEvaluatorResponse.status required")
    return out
