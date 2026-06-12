"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbInstanceVpcSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_group

AwsRdsDbInstanceVpcSecurityGroups: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_group.AwsRdsDbInstanceVpcSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbInstanceVpcSecurityGroups) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbInstanceVpcSecurityGroups:
    import aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_group

    out: AwsRdsDbInstanceVpcSecurityGroups = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_instance_vpc_security_group.deserialize_json(
                item
            )
        )
    return out
