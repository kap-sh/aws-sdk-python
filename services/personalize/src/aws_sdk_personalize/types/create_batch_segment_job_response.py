"""Generated from Smithy shape ``com.amazonaws.personalize#CreateBatchSegmentJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateBatchSegmentJobResponse(TypedDict):
    batch_segment_job_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the batch segment job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBatchSegmentJobResponse) -> dict:
    out: dict = {}
    if "batch_segment_job_arn" in value:
        out["batchSegmentJobArn"] = value["batch_segment_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBatchSegmentJobResponse:
    out: CreateBatchSegmentJobResponse = {}  # type: ignore[typeddict-item]
    if "batchSegmentJobArn" in data:
        out["batch_segment_job_arn"] = data["batchSegmentJobArn"]
    return out
