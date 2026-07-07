"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeBatchInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.batch_inference_job


class DescribeBatchInferenceJobResponse(TypedDict, closed=True):
    batch_inference_job: NotRequired[
        "aws_sdk_personalize.types.batch_inference_job.BatchInferenceJob"
    ]
    """<p>Information on the specified batch inference job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchInferenceJobResponse) -> dict:
    out: dict = {}
    if "batch_inference_job" in value:
        import aws_sdk_personalize.types.batch_inference_job

        out["batchInferenceJob"] = (
            aws_sdk_personalize.types.batch_inference_job.serialize_aws_json_1_1(
                value["batch_inference_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchInferenceJobResponse:
    out: DescribeBatchInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "batchInferenceJob" in data:
        import aws_sdk_personalize.types.batch_inference_job

        out["batch_inference_job"] = (
            aws_sdk_personalize.types.batch_inference_job.deserialize_aws_json_1_1(
                data["batchInferenceJob"]
            )
        )
    return out
