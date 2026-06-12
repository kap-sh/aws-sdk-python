"""Generated from Smithy shape ``com.amazonaws.bedrock#BatchDeleteEvaluationJobError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_identifier


class BatchDeleteEvaluationJobError(TypedDict):
    job_identifier: (
        "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The ARN of the evaluation job being deleted.</p>"""
    code: "str"
    """<p>A HTTP status code of the evaluation job being deleted.</p>"""
    message: NotRequired["str"]
    """<p>A status message about the evaluation job deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteEvaluationJobError) -> dict:
    out: dict = {}
    out["jobIdentifier"] = value["job_identifier"]
    out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteEvaluationJobError:
    out: BatchDeleteEvaluationJobError = {}  # type: ignore[typeddict-item]
    if "jobIdentifier" in data:
        out["job_identifier"] = data["jobIdentifier"]
    else:
        raise DeserializationError(
            "BatchDeleteEvaluationJobError.job_identifier required"
        )
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchDeleteEvaluationJobError.code required")
    if "message" in data:
        out["message"] = data["message"]
    return out
