"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_jobs_list_member

RestoreJobsList: TypeAlias = list[
    "aws_sdk_backup.types.restore_jobs_list_member.RestoreJobsListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreJobsList) -> list:
    import aws_sdk_backup.types.restore_jobs_list_member

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.restore_jobs_list_member.serialize_json(item))
    return out


def deserialize_json(data: list) -> RestoreJobsList:
    import aws_sdk_backup.types.restore_jobs_list_member

    out: RestoreJobsList = []
    for item in data:
        out.append(aws_sdk_backup.types.restore_jobs_list_member.deserialize_json(item))
    return out
