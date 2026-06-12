"""Generated from Smithy shape ``com.amazonaws.snowball#JobListEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_list_entry

JobListEntryList: TypeAlias = list["aws_sdk_snowball.types.job_list_entry.JobListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobListEntryList) -> list:
    import aws_sdk_snowball.types.job_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_snowball.types.job_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobListEntryList:
    import aws_sdk_snowball.types.job_list_entry

    out: JobListEntryList = []
    for item in data:
        out.append(aws_sdk_snowball.types.job_list_entry.deserialize_aws_json_1_1(item))
    return out
