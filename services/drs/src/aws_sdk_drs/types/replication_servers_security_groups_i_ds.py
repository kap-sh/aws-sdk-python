"""Generated from Smithy shape ``com.amazonaws.drs#ReplicationServersSecurityGroupsIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.security_group_id

ReplicationServersSecurityGroupsIDs: TypeAlias = list[
    "aws_sdk_drs.types.security_group_id.SecurityGroupID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationServersSecurityGroupsIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> ReplicationServersSecurityGroupsIDs:
    return list(data)
