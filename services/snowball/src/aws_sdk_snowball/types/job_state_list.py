"""Generated from Smithy shape ``com.amazonaws.snowball#JobStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_state

JobStateList: TypeAlias = list["aws_sdk_snowball.types.job_state.JobState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStateList) -> list:
    import aws_sdk_snowball.types.job_state

    out: list = []
    for item in value:
        out.append(aws_sdk_snowball.types.job_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobStateList:
    import aws_sdk_snowball.types.job_state

    out: JobStateList = []
    for item in data:
        out.append(aws_sdk_snowball.types.job_state.deserialize_aws_json_1_1(item))
    return out
