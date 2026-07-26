"""Generated from Smithy shape ``com.amazonaws.iot#JobTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.job_template_summary

JobTemplateSummaryList: TypeAlias = list[
    "capo_iot.types.job_template_summary.JobTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplateSummaryList) -> list:
    import capo_iot.types.job_template_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.job_template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobTemplateSummaryList:
    import capo_iot.types.job_template_summary

    out: JobTemplateSummaryList = []
    for item in data:
        out.append(capo_iot.types.job_template_summary.deserialize_json(item))
    return out
