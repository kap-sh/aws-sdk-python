"""Generated from Smithy shape ``com.amazonaws.mgn#JobLogs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.job_log

JobLogs: TypeAlias = list["capo_mgn.types.job_log.JobLog"]


# --- restJson1 ser/de ---
def serialize_json(value: JobLogs) -> list:
    import capo_mgn.types.job_log

    out: list = []
    for item in value:
        out.append(capo_mgn.types.job_log.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobLogs:
    import capo_mgn.types.job_log

    out: JobLogs = []
    for item in data:
        out.append(capo_mgn.types.job_log.deserialize_json(item))
    return out
