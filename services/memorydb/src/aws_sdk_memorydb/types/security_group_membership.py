"""Generated from Smithy shape ``com.amazonaws.memorydb#SecurityGroupMembership``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class SecurityGroupMembership(TypedDict):
    security_group_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The identifier of the security group.</p>"""
    status: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The status of the security group membership. The status changes whenever a security group is modified, or when the security groups assigned to a cluster are modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupMembership) -> dict:
    out: dict = {}
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroupMembership:
    out: SecurityGroupMembership = {}  # type: ignore[typeddict-item]
    if "SecurityGroupId" in data:
        out["security_group_id"] = data["SecurityGroupId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
