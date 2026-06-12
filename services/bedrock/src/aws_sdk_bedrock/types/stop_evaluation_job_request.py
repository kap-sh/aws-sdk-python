"""Generated from Smithy shape ``com.amazonaws.bedrock#StopEvaluationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_job_identifier


class StopEvaluationJobRequest(TypedDict):
    job_identifier: (
        "aws_sdk_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier"
    )
    """<p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopEvaluationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopEvaluationJobRequest:
    out: StopEvaluationJobRequest = {}  # type: ignore[typeddict-item]
    return out
