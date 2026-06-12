"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#VpcSecurityGroupMembership``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class VpcSecurityGroupMembership(TypedDict):
    vpc_security_group_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The VPC security group ID.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
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
