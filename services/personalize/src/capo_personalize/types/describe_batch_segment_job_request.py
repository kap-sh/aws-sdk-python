"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeBatchSegmentJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeBatchSegmentJobRequest(TypedDict, closed=True):
    batch_segment_job_arn: "capo_personalize.types.arn.Arn"
    """<p>The ARN of the batch segment job to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchSegmentJobRequest) -> dict:
    out: dict = {}
    out["batchSegmentJobArn"] = value["batch_segment_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchSegmentJobRequest:
    out: DescribeBatchSegmentJobRequest = {}  # type: ignore[typeddict-item]
    if "batchSegmentJobArn" in data:
        out["batch_segment_job_arn"] = data["batchSegmentJobArn"]
    else:
        raise DeserializationError(
            "DescribeBatchSegmentJobRequest.batch_segment_job_arn required"
        )
    return out
