"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_entity

BatchGetJobEntityList: TypeAlias = list["aws_sdk_deadline.types.job_entity.JobEntity"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobEntityList) -> list:
    import aws_sdk_deadline.types.job_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.job_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetJobEntityList:
    import aws_sdk_deadline.types.job_entity

    out: BatchGetJobEntityList = []
    for item in data:
        out.append(aws_sdk_deadline.types.job_entity.deserialize_json(item))
    return out
