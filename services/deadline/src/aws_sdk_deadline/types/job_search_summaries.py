"""Generated from Smithy shape ``com.amazonaws.deadline#JobSearchSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_search_summary

JobSearchSummaries: TypeAlias = list[
    "aws_sdk_deadline.types.job_search_summary.JobSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobSearchSummaries) -> list:
    import aws_sdk_deadline.types.job_search_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.job_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobSearchSummaries:
    import aws_sdk_deadline.types.job_search_summary

    out: JobSearchSummaries = []
    for item in data:
        out.append(aws_sdk_deadline.types.job_search_summary.deserialize_json(item))
    return out
