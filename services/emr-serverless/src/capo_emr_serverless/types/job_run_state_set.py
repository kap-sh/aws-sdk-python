"""Generated from Smithy shape ``com.amazonaws.emrserverless#JobRunStateSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.job_run_state

JobRunStateSet: TypeAlias = list["capo_emr_serverless.types.job_run_state.JobRunState"]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunStateSet) -> list:
    return list(value)


def deserialize_json(data: list) -> JobRunStateSet:
    return list(data)
