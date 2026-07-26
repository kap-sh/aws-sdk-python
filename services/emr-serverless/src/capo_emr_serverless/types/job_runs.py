"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRuns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.job_run_summary

JobRuns: TypeAlias = list["capo_emr_serverless.types.job_run_summary.JobRunSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRuns) -> list:
    import capo_emr_serverless.types.job_run_summary

    out: list = []
    for item in value:
        out.append(capo_emr_serverless.types.job_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobRuns:
    import capo_emr_serverless.types.job_run_summary

    out: JobRuns = []
    for item in data:
        out.append(capo_emr_serverless.types.job_run_summary.deserialize_json(item))
    return out
