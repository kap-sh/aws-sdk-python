"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartBatchEvaluationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.batch_evaluation_arn
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.batch_evaluation_status
    import capo_bedrock_agentcore.types.evaluator_list
    import capo_bedrock_agentcore.types.output_config


class StartBatchEvaluationResponse(TypedDict, closed=True):
    batch_evaluation_id: (
        "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    )
    """<p>The unique identifier of the created batch evaluation.</p>"""
    batch_evaluation_arn: (
        "capo_bedrock_agentcore.types.batch_evaluation_arn.BatchEvaluationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created batch evaluation.</p>"""
    batch_evaluation_name: (
        "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName"
    )
    """<p>The name of the batch evaluation.</p>"""
    evaluators: NotRequired["capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"]
    """<p>The list of evaluators applied during the batch evaluation.</p>"""
    status: "capo_bedrock_agentcore.types.batch_evaluation_status.BatchEvaluationStatus"
    """<p>The status of the batch evaluation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the batch evaluation was created.</p>"""
    output_config: NotRequired[
        "capo_bedrock_agentcore.types.output_config.OutputConfig"
    ]
    """<p>The output configuration specifying where evaluation results are written.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
    ]
    """<p>The description of the batch evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBatchEvaluationResponse) -> dict:
    out: dict = {}
    out["batchEvaluationId"] = value["batch_evaluation_id"]
    out["batchEvaluationArn"] = value["batch_evaluation_arn"]
    out["batchEvaluationName"] = value["batch_evaluation_name"]
    if "evaluators" in value:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = capo_bedrock_agentcore.types.evaluator_list.serialize_json(
            value["evaluators"]
        )
    import capo_bedrock_agentcore.types.batch_evaluation_status

    out["status"] = capo_bedrock_agentcore.types.batch_evaluation_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "output_config" in value:
        import capo_bedrock_agentcore.types.output_config

        out["outputConfig"] = capo_bedrock_agentcore.types.output_config.serialize_json(
            value["output_config"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StartBatchEvaluationResponse:
    out: StartBatchEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "batchEvaluationId" in data:
        out["batch_evaluation_id"] = data["batchEvaluationId"]
    else:
        raise DeserializationError(
            "StartBatchEvaluationResponse.batch_evaluation_id required"
        )
    if "batchEvaluationArn" in data:
        out["batch_evaluation_arn"] = data["batchEvaluationArn"]
    else:
        raise DeserializationError(
            "StartBatchEvaluationResponse.batch_evaluation_arn required"
        )
    if "batchEvaluationName" in data:
        out["batch_evaluation_name"] = data["batchEvaluationName"]
    else:
        raise DeserializationError(
            "StartBatchEvaluationResponse.batch_evaluation_name required"
        )
    if "evaluators" in data:
        import capo_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    if "status" in data:
        import capo_bedrock_agentcore.types.batch_evaluation_status

        out["status"] = (
            capo_bedrock_agentcore.types.batch_evaluation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StartBatchEvaluationResponse.status required")
    if "createdAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("StartBatchEvaluationResponse.created_at required")
    if "outputConfig" in data:
        import capo_bedrock_agentcore.types.output_config

        out["output_config"] = (
            capo_bedrock_agentcore.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
