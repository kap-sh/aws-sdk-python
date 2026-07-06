"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_identifier
    import aws_sdk_bedrock.types.evaluation_job_status


class BatchDeleteEvaluationJobItem(TypedDict, closed=True):
    job_identifier: (
        "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluation job for deletion.</p>"""
    job_status: "aws_sdk_bedrock.types.evaluation_job_status.EvaluationJobStatus"
    """<p>The status of the evaluation job for deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobItem) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    import aws_sdk_bedrock.types.evaluation_job_status

    out["jobStatus"] = aws_sdk_bedrock.types.evaluation_job_status.serialize_json(
        value["job_status"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobItem:
    out: BatchDeleteEvaluationJobItem = {}  # type: ignore[typeddict-item]
    if "jobIdentifier" in data:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        raise DeserializationError(
            "BatchDeleteEvaluationJobItem.job_identifier required"
        )
    if "jobStatus" in data:
        import aws_sdk_bedrock.types.evaluation_job_status

        out["job_status"] = (
            aws_sdk_bedrock.types.evaluation_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteEvaluationJobItem.job_status required")
    return out
