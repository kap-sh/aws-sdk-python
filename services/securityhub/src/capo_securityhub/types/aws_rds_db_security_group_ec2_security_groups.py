"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSecurityGroupEc2SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_security_group_ec2_security_group

AwsRdsDbSecurityGroupEc2SecurityGroups: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_security_group_ec2_security_group.AwsRdsDbSecurityGroupEc2SecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSecurityGroupEc2SecurityGroups) -> list:
    import capo_securityhub.types.aws_rds_db_security_group_ec2_security_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_security_group_ec2_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbSecurityGroupEc2SecurityGroups:
    import capo_securityhub.types.aws_rds_db_security_group_ec2_security_group

    out: AwsRdsDbSecurityGroupEc2SecurityGroups = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_security_group_ec2_security_group.deserialize_json(
                item
            )
        )
    return out
