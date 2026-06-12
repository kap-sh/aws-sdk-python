"""Generated from Smithy shape ``com.amazonaws.drs#JobLogs``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.job_log

JobLogs: TypeAlias = list["aws_sdk_drs.types.job_log.JobLog"]


# --- restJson1 ser/de ---
def serialize_json(value: JobLogs) -> list:
    import aws_sdk_drs.types.job_log
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.job_log.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobLogs:
    import aws_sdk_drs.types.job_log
    out: JobLogs = []
    for item in data:
        out.append(aws_sdk_drs.types.job_log.deserialize_json(item))
    return out