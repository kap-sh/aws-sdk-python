"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#VpcSecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class VpcSecurityGroupMembership(TypedDict, closed=True):
    vpc_security_group_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The VPC security group ID.</p>"""
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The status of the VPC security group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSecurityGroupMembership) -> dict:
    out: dict = {}
    if "vpc_security_group_id" in value:
        out["VpcSecurityGroupId"] = value["vpc_security_group_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcSecurityGroupMembership:
    out: VpcSecurityGroupMembership = {}  # type: ignore[typeddict-item]
    if "VpcSecurityGroupId" in data:
        out["vpc_security_group_id"] = data["VpcSecurityGroupId"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
