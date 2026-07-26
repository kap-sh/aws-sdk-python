"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_connections.types.security_group_id

SecurityGroupIds: TypeAlias = list[
    "capo_codestar_connections.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupIds:
    return list(data)
