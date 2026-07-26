"""Generated from Smithy shape ``com.amazonaws.personalize#CreateBatchInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class CreateBatchInferenceJobResponse(TypedDict, closed=True):
    batch_inference_job_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the batch inference job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchInferenceJobResponse) -> dict:
    out: dict = {}
    if "batch_inference_job_arn" in value:
        out["batchInferenceJobArn"] = value["batch_inference_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchInferenceJobResponse:
    out: CreateBatchInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "batchInferenceJobArn" in data:
        out["batch_inference_job_arn"] = data["batchInferenceJobArn"]
    return out
