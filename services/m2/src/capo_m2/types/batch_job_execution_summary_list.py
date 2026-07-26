"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.batch_job_execution_summary

BatchJobExecutionSummaryList: TypeAlias = list[
    "capo_m2.types.batch_job_execution_summary.BatchJobExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobExecutionSummaryList) -> list:
    import capo_m2.types.batch_job_execution_summary

    out: list = []
    for item in value:
        out.append(capo_m2.types.batch_job_execution_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchJobExecutionSummaryList:
    import capo_m2.types.batch_job_execution_summary

    out: BatchJobExecutionSummaryList = []
    for item in data:
        out.append(capo_m2.types.batch_job_execution_summary.deserialize_json(item))
    return out
