"""Generated from Smithy shape ``com.amazonaws.batch#JobDependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.job_dependency

JobDependencyList: TypeAlias = list["aws_sdk_batch.types.job_dependency.JobDependency"]


# --- restJson1 ser/de ---
def serialize_json(value: JobDependencyList) -> list:
    import aws_sdk_batch.types.job_dependency

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.job_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobDependencyList:
    import aws_sdk_batch.types.job_dependency

    out: JobDependencyList = []
    for item in data:
        out.append(aws_sdk_batch.types.job_dependency.deserialize_json(item))
    return out
