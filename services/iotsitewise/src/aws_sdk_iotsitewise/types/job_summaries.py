"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.job_summary

JobSummaries: TypeAlias = list["aws_sdk_iotsitewise.types.job_summary.JobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobSummaries) -> list:
    import aws_sdk_iotsitewise.types.job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobSummaries:
    import aws_sdk_iotsitewise.types.job_summary

    out: JobSummaries = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.job_summary.deserialize_json(item))
    return out
