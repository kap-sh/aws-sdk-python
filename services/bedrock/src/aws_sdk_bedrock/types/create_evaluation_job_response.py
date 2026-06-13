"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateEvaluationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_arn


class CreateEvaluationJobResponse(TypedDict):
    job_arn: "aws_sdk_bedrock.types.evaluation_job_arn.EvaluationJobArn"
    """<p>The Amazon Resource Name (ARN) of the evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateEvaluationJobResponse:
    out: CreateEvaluationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("CreateEvaluationJobResponse.job_arn required")
    return out
