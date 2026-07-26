"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.job_step

BatchJobStepList: TypeAlias = list["capo_m2.types.job_step.JobStep"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobStepList) -> list:
    import capo_m2.types.job_step

    out: list = []
    for item in value:
        out.append(capo_m2.types.job_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchJobStepList:
    import capo_m2.types.job_step

    out: BatchJobStepList = []
    for item in data:
        out.append(capo_m2.types.job_step.deserialize_json(item))
    return out
