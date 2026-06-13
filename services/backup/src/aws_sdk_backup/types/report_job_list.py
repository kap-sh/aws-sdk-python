"""Generated from Smithy shape ``com.amazonaws.backup#ReportJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.report_job

ReportJobList: TypeAlias = list["aws_sdk_backup.types.report_job.ReportJob"]


# --- restJson1 ser/de ---
def serialize_json(value: ReportJobList) -> list:
    import aws_sdk_backup.types.report_job

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.report_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReportJobList:
    import aws_sdk_backup.types.report_job

    out: ReportJobList = []
    for item in data:
        out.append(aws_sdk_backup.types.report_job.deserialize_json(item))
    return out
