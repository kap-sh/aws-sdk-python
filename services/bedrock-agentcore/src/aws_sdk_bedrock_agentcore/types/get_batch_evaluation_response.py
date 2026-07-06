"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetBatchEvaluationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.batch_evaluation_arn
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_description
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_id
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_name
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_status
    import aws_sdk_bedrock_agentcore.types.data_source_config
    import aws_sdk_bedrock_agentcore.types.error_details_list
    import aws_sdk_bedrock_agentcore.types.evaluation_job_results
    import aws_sdk_bedrock_agentcore.types.evaluator_list
    import aws_sdk_bedrock_agentcore.types.output_config


class GetBatchEvaluationResponse(TypedDict, closed=True):
    batch_evaluation_id: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    )
    """<p>The unique identifier of the batch evaluation.</p>"""
    batch_evaluation_arn: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_arn.BatchEvaluationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the batch evaluation.</p>"""
    batch_evaluation_name: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName"
    )
    """<p>The name of the batch evaluation.</p>"""
    status: (
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_status.BatchEvaluationStatus"
    )
    """<p>The current status of the batch evaluation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the batch evaluation was created.</p>"""
    evaluators: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluator_list.EvaluatorList"
    ]
    """<p>The list of evaluators applied during the batch evaluation.</p>"""
    data_source_config: NotRequired[
        "aws_sdk_bedrock_agentcore.types.data_source_config.DataSourceConfig"
    ]
    """<p>The data source configuration specifying where agent traces are pulled from.</p>"""
    output_config: NotRequired[
        "aws_sdk_bedrock_agentcore.types.output_config.OutputConfig"
    ]
    """<p>The output configuration specifying where evaluation results are written.</p>"""
    evaluation_results: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_job_results.EvaluationJobResults"
    ]
    """<p>The aggregated evaluation results, including session completion counts and evaluator score summaries.</p>"""
    error_details: NotRequired[
        "aws_sdk_bedrock_agentcore.types.error_details_list.ErrorDetailsList"
    ]
    """<p>The error details if the batch evaluation encountered failures.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
    ]
    """<p>The description of the batch evaluation.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the batch evaluation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBatchEvaluationResponse) -> dict:
    out: dict = {}
    out["batchEvaluationId"] = value["batch_evaluation_id"]
    out["batchEvaluationArn"] = value["batch_evaluation_arn"]
    out["batchEvaluationName"] = value["batch_evaluation_name"]
    import aws_sdk_bedrock_agentcore.types.batch_evaluation_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.batch_evaluation_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    if "evaluators" in value:
        import aws_sdk_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_list.serialize_json(
                value["evaluators"]
            )
        )
    if "data_source_config" in value:
        import aws_sdk_bedrock_agentcore.types.data_source_config

        out["dataSourceConfig"] = (
            aws_sdk_bedrock_agentcore.types.data_source_config.serialize_json(
                value["data_source_config"]
            )
        )
    if "output_config" in value:
        import aws_sdk_bedrock_agentcore.types.output_config

        out["outputConfig"] = (
            aws_sdk_bedrock_agentcore.types.output_config.serialize_json(
                value["output_config"]
            )
        )
    if "evaluation_results" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_job_results

        out["evaluationResults"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_job_results.serialize_json(
                value["evaluation_results"]
            )
        )
    if "error_details" in value:
        import aws_sdk_bedrock_agentcore.types.error_details_list

        out["errorDetails"] = (
            aws_sdk_bedrock_agentcore.types.error_details_list.serialize_json(
                value["error_details"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "updated_at" in value:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBatchEvaluationResponse:
    out: GetBatchEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "batchEvaluationId" in data:
        out["batch_evaluation_id"] = data["batchEvaluationId"]
    else:
        raise DeserializationError(
            "GetBatchEvaluationResponse.batch_evaluation_id required"
        )
    if "batchEvaluationArn" in data:
        out["batch_evaluation_arn"] = data["batchEvaluationArn"]
    else:
        raise DeserializationError(
            "GetBatchEvaluationResponse.batch_evaluation_arn required"
        )
    if "batchEvaluationName" in data:
        out["batch_evaluation_name"] = data["batchEvaluationName"]
    else:
        raise DeserializationError(
            "GetBatchEvaluationResponse.batch_evaluation_name required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.batch_evaluation_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.batch_evaluation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetBatchEvaluationResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetBatchEvaluationResponse.created_at required")
    if "evaluators" in data:
        import aws_sdk_bedrock_agentcore.types.evaluator_list

        out["evaluators"] = (
            aws_sdk_bedrock_agentcore.types.evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    if "dataSourceConfig" in data:
        import aws_sdk_bedrock_agentcore.types.data_source_config

        out["data_source_config"] = (
            aws_sdk_bedrock_agentcore.types.data_source_config.deserialize_json(
                data["dataSourceConfig"]
            )
        )
    if "outputConfig" in data:
        import aws_sdk_bedrock_agentcore.types.output_config

        out["output_config"] = (
            aws_sdk_bedrock_agentcore.types.output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    if "evaluationResults" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_job_results

        out["evaluation_results"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_job_results.deserialize_json(
                data["evaluationResults"]
            )
        )
    if "errorDetails" in data:
        import aws_sdk_bedrock_agentcore.types.error_details_list

        out["error_details"] = (
            aws_sdk_bedrock_agentcore.types.error_details_list.deserialize_json(
                data["errorDetails"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
