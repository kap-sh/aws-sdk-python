"""Generated from Smithy shape ``com.amazonaws.efs#ModifyMountTargetSecurityGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.mount_target_id
    import aws_sdk_efs.types.security_groups


class ModifyMountTargetSecurityGroupsRequest(TypedDict):
    mount_target_id: "aws_sdk_efs.types.mount_target_id.MountTargetId"
    """<p>The ID of the mount target whose security groups you want to modify.</p>"""
    security_groups: NotRequired["aws_sdk_efs.types.security_groups.SecurityGroups"]
    """<p>An array of VPC security group IDs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyMountTargetSecurityGroupsRequest) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import aws_sdk_efs.types.security_groups

        out["SecurityGroups"] = aws_sdk_efs.types.security_groups.serialize_json(
            value["security_groups"]
        )
    return out


def deserialize_json(data: dict) -> ModifyMountTargetSecurityGroupsRequest:
    out: ModifyMountTargetSecurityGroupsRequest = {}  # type: ignore[typeddict-item]
    if "SecurityGroups" in data:
        import aws_sdk_efs.types.security_groups

        out["security_groups"] = aws_sdk_efs.types.security_groups.deserialize_json(
            data["SecurityGroups"]
        )
    return out
