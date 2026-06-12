"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.export_job_summary

ExportJobSummaryList: TypeAlias = list[
    "aws_sdk_sesv2.types.export_job_summary.ExportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportJobSummaryList) -> list:
    import aws_sdk_sesv2.types.export_job_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.export_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportJobSummaryList:
    import aws_sdk_sesv2.types.export_job_summary

    out: ExportJobSummaryList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.export_job_summary.deserialize_json(item))
    return out
