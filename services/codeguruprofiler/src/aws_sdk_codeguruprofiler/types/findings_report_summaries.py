"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FindingsReportSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.findings_report_summary

FindingsReportSummaries: TypeAlias = list[
    "aws_sdk_codeguruprofiler.types.findings_report_summary.FindingsReportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsReportSummaries) -> list:
    import aws_sdk_codeguruprofiler.types.findings_report_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguruprofiler.types.findings_report_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsReportSummaries:
    import aws_sdk_codeguruprofiler.types.findings_report_summary

    out: FindingsReportSummaries = []
    for item in data:
        out.append(
            aws_sdk_codeguruprofiler.types.findings_report_summary.deserialize_json(
                item
            )
        )
    return out
