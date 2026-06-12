"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsReplicationInstanceVpcSecurityGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details

AwsDmsReplicationInstanceVpcSecurityGroupsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details.AwsDmsReplicationInstanceVpcSecurityGroupsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDmsReplicationInstanceVpcSecurityGroupsList) -> list:
    import aws_sdk_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDmsReplicationInstanceVpcSecurityGroupsList:
    import aws_sdk_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details

    out: AwsDmsReplicationInstanceVpcSecurityGroupsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details.deserialize_json(
                item
            )
        )
    return out
