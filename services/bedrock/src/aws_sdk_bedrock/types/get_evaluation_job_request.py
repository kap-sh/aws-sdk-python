"""Generated from Smithy shape ``com.amazonaws.bedrock#GetEvaluationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_identifier


class GetEvaluationJobRequest(TypedDict):
    job_identifier: (
        "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEvaluationJobRequest:
    out: GetEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    return out
