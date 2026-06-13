"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.import_job

ImportJobs: TypeAlias = list["aws_sdk_mailmanager.types.import_job.ImportJob"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJobs) -> list:
    import aws_sdk_mailmanager.types.import_job

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.import_job.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ImportJobs:
    import aws_sdk_mailmanager.types.import_job

    out: ImportJobs = []
    for item in data:
        out.append(aws_sdk_mailmanager.types.import_job.deserialize_aws_json_1_0(item))
    return out
