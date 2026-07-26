"""Generated from Smithy shape ``com.amazonaws.personalize#BatchSegmentJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.batch_segment_job_summary

BatchSegmentJobs: TypeAlias = list[
    "capo_personalize.types.batch_segment_job_summary.BatchSegmentJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchSegmentJobs) -> list:
    import capo_personalize.types.batch_segment_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.batch_segment_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchSegmentJobs:
    import capo_personalize.types.batch_segment_job_summary

    out: BatchSegmentJobs = []
    for item in data:
        out.append(
            capo_personalize.types.batch_segment_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
