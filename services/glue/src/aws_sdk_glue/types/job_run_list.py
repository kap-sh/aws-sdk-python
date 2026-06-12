"""Generated from Smithy shape ``com.amazonaws.glue#JobRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.job_run

JobRunList: TypeAlias = list["aws_sdk_glue.types.job_run.JobRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobRunList) -> list:
    import aws_sdk_glue.types.job_run

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.job_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobRunList:
    import aws_sdk_glue.types.job_run

    out: JobRunList = []
    for item in data:
        out.append(aws_sdk_glue.types.job_run.deserialize_aws_json_1_1(item))
    return out
