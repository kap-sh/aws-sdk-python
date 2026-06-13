"""Generated from Smithy shape ``com.amazonaws.braket#JobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.job_summary

JobSummaryList: TypeAlias = list["aws_sdk_braket.types.job_summary.JobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobSummaryList) -> list:
    import aws_sdk_braket.types.job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_braket.types.job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobSummaryList:
    import aws_sdk_braket.types.job_summary

    out: JobSummaryList = []
    for item in data:
        out.append(aws_sdk_braket.types.job_summary.deserialize_json(item))
    return out
