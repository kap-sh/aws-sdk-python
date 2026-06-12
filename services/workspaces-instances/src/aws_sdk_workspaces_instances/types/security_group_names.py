"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SecurityGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.security_group_name

SecurityGroupNames: TypeAlias = list["aws_sdk_workspaces_instances.types.security_group_name.SecurityGroupName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroupNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroupNames:
    return list(data)