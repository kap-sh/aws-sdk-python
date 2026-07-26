"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.work_group_name

WorkGroupNamesList: TypeAlias = list["capo_athena.types.work_group_name.WorkGroupName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkGroupNamesList:
    return list(data)
