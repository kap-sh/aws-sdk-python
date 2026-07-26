"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSubnetGroupSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_subnet_group_subnet

AwsRdsDbSubnetGroupSubnets: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_subnet_group_subnet.AwsRdsDbSubnetGroupSubnet"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSubnetGroupSubnets) -> list:
    import capo_securityhub.types.aws_rds_db_subnet_group_subnet

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_subnet_group_subnet.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbSubnetGroupSubnets:
    import capo_securityhub.types.aws_rds_db_subnet_group_subnet

    out: AwsRdsDbSubnetGroupSubnets = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_subnet_group_subnet.deserialize_json(item)
        )
    return out
