"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListOfSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.security_group_id

ListOfSecurityGroupIds: TypeAlias = list[
    "aws_sdk_devops_agent.types.security_group_id.SecurityGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfSecurityGroupIds:
    return list(data)
