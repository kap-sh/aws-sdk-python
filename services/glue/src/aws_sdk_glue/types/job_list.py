"""Generated from Smithy shape ``com.amazonaws.glue#JobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.job

JobList: TypeAlias = list["aws_sdk_glue.types.job.Job"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobList) -> list:
    import aws_sdk_glue.types.job

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.job.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobList:
    import aws_sdk_glue.types.job

    out: JobList = []
    for item in data:
        out.append(aws_sdk_glue.types.job.deserialize_aws_json_1_1(item))
    return out
