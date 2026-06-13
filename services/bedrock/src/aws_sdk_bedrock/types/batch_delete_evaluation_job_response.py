"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_errors
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_items


class BatchDeleteEvaluationJobResponse(TypedDict):
    errors: "aws_sdk_bedrock.types.batch_delete_evaluation_job_errors.BatchDeleteEvaluationJobErrors"
    """<p>A JSON object containing the HTTP status codes and the ARNs of evaluation jobs that failed to be deleted.</p>"""
    evaluation_jobs: "aws_sdk_bedrock.types.batch_delete_evaluation_job_items.BatchDeleteEvaluationJobItems"
    """<p>The list of evaluation jobs for deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_errors

    out["errors"] = (
        aws_sdk_bedrock.types.batch_delete_evaluation_job_errors.serialize_json(
            value["errors"]
        )
    )
    import aws_sdk_bedrock.types.batch_delete_evaluation_job_items

    out["evaluationJobs"] = (
        aws_sdk_bedrock.types.batch_delete_evaluation_job_items.serialize_json(
            value["evaluation_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobResponse:
    out: BatchDeleteEvaluationJobResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_bedrock.types.batch_delete_evaluation_job_errors

        out["errors"] = (
            aws_sdk_bedrock.types.batch_delete_evaluation_job_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteEvaluationJobResponse.errors required")
    if "evaluationJobs" in data:
        import aws_sdk_bedrock.types.batch_delete_evaluation_job_items

        out["evaluation_jobs"] = (
            aws_sdk_bedrock.types.batch_delete_evaluation_job_items.deserialize_json(
                data["evaluationJobs"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteEvaluationJobResponse.evaluation_jobs required"
        )
    return out
