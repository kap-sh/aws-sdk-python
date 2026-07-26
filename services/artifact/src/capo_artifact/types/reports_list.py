"""Generated from Smithy shape ``com.amazonaws.artifact#ReportsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_artifact.types.report_summary

ReportsList: TypeAlias = list["capo_artifact.types.report_summary.ReportSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ReportsList) -> list:
    import capo_artifact.types.report_summary

    out: list = []
    for item in value:
        out.append(capo_artifact.types.report_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReportsList:
    import capo_artifact.types.report_summary

    out: ReportsList = []
    for item in data:
        out.append(capo_artifact.types.report_summary.deserialize_json(item))
    return out
