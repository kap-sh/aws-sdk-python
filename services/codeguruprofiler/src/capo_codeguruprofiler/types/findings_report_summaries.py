"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FindingsReportSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.findings_report_summary

FindingsReportSummaries: TypeAlias = list[
    "capo_codeguruprofiler.types.findings_report_summary.FindingsReportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsReportSummaries) -> list:
    import capo_codeguruprofiler.types.findings_report_summary

    out: list = []
    for item in value:
        out.append(
            capo_codeguruprofiler.types.findings_report_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsReportSummaries:
    import capo_codeguruprofiler.types.findings_report_summary

    out: FindingsReportSummaries = []
    for item in data:
        out.append(
            capo_codeguruprofiler.types.findings_report_summary.deserialize_json(item)
        )
    return out
