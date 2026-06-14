"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateEvaluatorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.evaluator_arn
    import aws_sdk_bedrock_agentcore_control.types.evaluator_id
    import aws_sdk_bedrock_agentcore_control.types.evaluator_status


class UpdateEvaluatorResponse(TypedDict):
    evaluator_arn: "aws_sdk_bedrock_agentcore_control.types.evaluator_arn.EvaluatorArn"
    """<p> The Amazon Resource Name (ARN) of the updated evaluator. </p>"""
    evaluator_id: "aws_sdk_bedrock_agentcore_control.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the updated evaluator. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the evaluator was last updated. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.evaluator_status.EvaluatorStatus"
    """<p> The status of the evaluator update operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEvaluatorResponse) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    out["evaluatorId"] = value["evaluator_id"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.evaluator_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.evaluator_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateEvaluatorResponse:
    out: UpdateEvaluatorResponse = {}  # type: ignore[typeddict-item]
    if "evaluatorArn" in data:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        raise DeserializationError("UpdateEvaluatorResponse.evaluator_arn required")
    if "evaluatorId" in data:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        raise DeserializationError("UpdateEvaluatorResponse.evaluator_id required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateEvaluatorResponse.updated_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateEvaluatorResponse.status required")
    return out
