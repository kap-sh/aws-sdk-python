"""Generated from Smithy shape ``com.amazonaws.batch#JobDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.job_definition

JobDefinitionList: TypeAlias = list["aws_sdk_batch.types.job_definition.JobDefinition"]


# --- restJson1 ser/de ---
def serialize_json(value: JobDefinitionList) -> list:
    import aws_sdk_batch.types.job_definition

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.job_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobDefinitionList:
    import aws_sdk_batch.types.job_definition

    out: JobDefinitionList = []
    for item in data:
        out.append(aws_sdk_batch.types.job_definition.deserialize_json(item))
    return out
