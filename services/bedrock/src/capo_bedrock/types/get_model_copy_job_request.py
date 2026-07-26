"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelCopyJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_copy_job_arn


class GetModelCopyJobRequest(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_copy_job_arn.ModelCopyJobArn"
    """<p>The Amazon Resource Name (ARN) of the model copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelCopyJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelCopyJobRequest:
    out: GetModelCopyJobRequest = {}  # type: ignore[typeddict-item]
    return out
