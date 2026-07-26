"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.service_job_summary

ServiceJobSummaryList: TypeAlias = list[
    "capo_batch.types.service_job_summary.ServiceJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobSummaryList) -> list:
    import capo_batch.types.service_job_summary

    out: list = []
    for item in value:
        out.append(capo_batch.types.service_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceJobSummaryList:
    import capo_batch.types.service_job_summary

    out: ServiceJobSummaryList = []
    for item in data:
        out.append(capo_batch.types.service_job_summary.deserialize_json(item))
    return out
