"""Generated from Smithy shape ``com.amazonaws.batch#JobQueueDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.job_queue_detail

JobQueueDetailList: TypeAlias = list[
    "aws_sdk_batch.types.job_queue_detail.JobQueueDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobQueueDetailList) -> list:
    import aws_sdk_batch.types.job_queue_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.job_queue_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobQueueDetailList:
    import aws_sdk_batch.types.job_queue_detail

    out: JobQueueDetailList = []
    for item in data:
        out.append(aws_sdk_batch.types.job_queue_detail.deserialize_json(item))
    return out
