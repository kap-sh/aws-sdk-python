"""Generated from Smithy shape ``com.amazonaws.deadline#JobMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.job_member

JobMembers: TypeAlias = list["aws_sdk_deadline.types.job_member.JobMember"]


# --- restJson1 ser/de ---
def serialize_json(value: JobMembers) -> list:
    import aws_sdk_deadline.types.job_member

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.job_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> JobMembers:
    import aws_sdk_deadline.types.job_member

    out: JobMembers = []
    for item in data:
        out.append(aws_sdk_deadline.types.job_member.deserialize_json(item))
    return out
