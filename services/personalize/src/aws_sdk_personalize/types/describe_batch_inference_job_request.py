"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeBatchInferenceJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeBatchInferenceJobRequest(TypedDict):
    batch_inference_job_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The ARN of the batch inference job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchInferenceJobRequest) -> dict:
    out: dict = {}
    out["batchInferenceJobArn"] = value["batch_inference_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchInferenceJobRequest:
    out: DescribeBatchInferenceJobRequest = {}  # type: ignore[typeddict-item]
    if "batchInferenceJobArn" in data:
        out["batch_inference_job_arn"] = data["batchInferenceJobArn"]
    else:
        raise DeserializationError(
            "DescribeBatchInferenceJobRequest.batch_inference_job_arn required"
        )
    return out
