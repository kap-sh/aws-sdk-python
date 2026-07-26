"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeBatchSegmentJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.batch_segment_job


class DescribeBatchSegmentJobResponse(TypedDict, closed=True):
    batch_segment_job: NotRequired[
        "capo_personalize.types.batch_segment_job.BatchSegmentJob"
    ]
    """<p>Information on the specified batch segment job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchSegmentJobResponse) -> dict:
    out: dict = {}
    if "batch_segment_job" in value:
        import capo_personalize.types.batch_segment_job

        out["batchSegmentJob"] = (
            capo_personalize.types.batch_segment_job.serialize_aws_json_1_1(
                value["batch_segment_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchSegmentJobResponse:
    out: DescribeBatchSegmentJobResponse = {}  # type: ignore[typeddict-item]
    if "batchSegmentJob" in data:
        import capo_personalize.types.batch_segment_job

        out["batch_segment_job"] = (
            capo_personalize.types.batch_segment_job.deserialize_aws_json_1_1(
                data["batchSegmentJob"]
            )
        )
    return out
