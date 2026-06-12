"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.batch_load_task

BatchLoadTaskList: TypeAlias = list[
    "aws_sdk_timestream_write.types.batch_load_task.BatchLoadTask"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadTaskList) -> list:
    import aws_sdk_timestream_write.types.batch_load_task

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_write.types.batch_load_task.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchLoadTaskList:
    import aws_sdk_timestream_write.types.batch_load_task

    out: BatchLoadTaskList = []
    for item in data:
        out.append(
            aws_sdk_timestream_write.types.batch_load_task.deserialize_aws_json_1_0(
                item
            )
        )
    return out
