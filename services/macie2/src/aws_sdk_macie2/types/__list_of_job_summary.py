"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfJobSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.job_summary

__listOfJobSummary: TypeAlias = list["aws_sdk_macie2.types.job_summary.JobSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfJobSummary) -> list:
    import aws_sdk_macie2.types.job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfJobSummary:
    import aws_sdk_macie2.types.job_summary

    out: __listOfJobSummary = []
    for item in data:
        out.append(aws_sdk_macie2.types.job_summary.deserialize_json(item))
    return out
