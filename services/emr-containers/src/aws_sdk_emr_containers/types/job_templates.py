"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobTemplates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.job_template

JobTemplates: TypeAlias = list["aws_sdk_emr_containers.types.job_template.JobTemplate"]


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplates) -> list:
    import aws_sdk_emr_containers.types.job_template

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_containers.types.job_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobTemplates:
    import aws_sdk_emr_containers.types.job_template

    out: JobTemplates = []
    for item in data:
        out.append(aws_sdk_emr_containers.types.job_template.deserialize_json(item))
    return out
