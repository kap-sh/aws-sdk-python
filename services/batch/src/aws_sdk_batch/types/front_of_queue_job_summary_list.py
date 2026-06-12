"""Generated from Smithy shape ``com.amazonaws.batch#FrontOfQueueJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.front_of_queue_job_summary

FrontOfQueueJobSummaryList: TypeAlias = list[
    "aws_sdk_batch.types.front_of_queue_job_summary.FrontOfQueueJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrontOfQueueJobSummaryList) -> list:
    import aws_sdk_batch.types.front_of_queue_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.front_of_queue_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FrontOfQueueJobSummaryList:
    import aws_sdk_batch.types.front_of_queue_job_summary

    out: FrontOfQueueJobSummaryList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.front_of_queue_job_summary.deserialize_json(item)
        )
    return out
