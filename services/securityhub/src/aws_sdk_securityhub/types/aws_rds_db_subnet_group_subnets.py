"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSubnetGroupSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnet

AwsRdsDbSubnetGroupSubnets: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnet.AwsRdsDbSubnetGroupSubnet"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSubnetGroupSubnets) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnet

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnet.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbSubnetGroupSubnets:
    import aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnet

    out: AwsRdsDbSubnetGroupSubnets = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_subnet_group_subnet.deserialize_json(
                item
            )
        )
    return out
