"""Generated from Smithy shape ``com.amazonaws.fsx#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.security_group_id

SecurityGroupIds: TypeAlias = list["capo_fsx.types.security_group_id.SecurityGroupId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupIds:
    return list(data)
