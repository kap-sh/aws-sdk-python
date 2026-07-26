"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsReplicationInstanceVpcSecurityGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details

AwsDmsReplicationInstanceVpcSecurityGroupsList: TypeAlias = list[
    "capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details.AwsDmsReplicationInstanceVpcSecurityGroupsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDmsReplicationInstanceVpcSecurityGroupsList) -> list:
    import capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDmsReplicationInstanceVpcSecurityGroupsList:
    import capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details

    out: AwsDmsReplicationInstanceVpcSecurityGroupsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_details.deserialize_json(
                item
            )
        )
    return out
