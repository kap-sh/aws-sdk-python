"""Generated from Smithy shape ``com.amazonaws.batch#JobDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.job_detail

JobDetailList: TypeAlias = list["capo_batch.types.job_detail.JobDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailList) -> list:
    import capo_batch.types.job_detail

    out: list = []
    for item in value:
        out.append(capo_batch.types.job_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobDetailList:
    import capo_batch.types.job_detail

    out: JobDetailList = []
    for item in data:
        out.append(capo_batch.types.job_detail.deserialize_json(item))
    return out
