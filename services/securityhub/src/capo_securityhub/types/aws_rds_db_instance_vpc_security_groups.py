"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceVpcSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_instance_vpc_security_group

AwsRdsDbInstanceVpcSecurityGroups: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_instance_vpc_security_group.AwsRdsDbInstanceVpcSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceVpcSecurityGroups) -> list:
    import capo_securityhub.types.aws_rds_db_instance_vpc_security_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_instance_vpc_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbInstanceVpcSecurityGroups:
    import capo_securityhub.types.aws_rds_db_instance_vpc_security_group

    out: AwsRdsDbInstanceVpcSecurityGroups = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_instance_vpc_security_group.deserialize_json(
                item
            )
        )
    return out
