"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_stop_job_run_error

BatchStopJobRunErrorList: TypeAlias = list[
    "aws_sdk_glue.types.batch_stop_job_run_error.BatchStopJobRunError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunErrorList) -> list:
    import aws_sdk_glue.types.batch_stop_job_run_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.batch_stop_job_run_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchStopJobRunErrorList:
    import aws_sdk_glue.types.batch_stop_job_run_error

    out: BatchStopJobRunErrorList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.batch_stop_job_run_error.deserialize_aws_json_1_1(item)
        )
    return out
