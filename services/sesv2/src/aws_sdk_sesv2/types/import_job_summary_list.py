"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.import_job_summary

ImportJobSummaryList: TypeAlias = list[
    "aws_sdk_sesv2.types.import_job_summary.ImportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobSummaryList) -> list:
    import aws_sdk_sesv2.types.import_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.import_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportJobSummaryList:
    import aws_sdk_sesv2.types.import_job_summary

    out: ImportJobSummaryList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.import_job_summary.deserialize_json(item))
    return out
