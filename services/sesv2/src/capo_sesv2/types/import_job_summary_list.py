"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.import_job_summary

ImportJobSummaryList: TypeAlias = list[
    "capo_sesv2.types.import_job_summary.ImportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobSummaryList) -> list:
    import capo_sesv2.types.import_job_summary

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.import_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportJobSummaryList:
    import capo_sesv2.types.import_job_summary

    out: ImportJobSummaryList = []
    for item in data:
        out.append(capo_sesv2.types.import_job_summary.deserialize_json(item))
    return out
