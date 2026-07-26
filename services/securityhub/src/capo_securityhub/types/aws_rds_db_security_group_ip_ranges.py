"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSecurityGroupIpRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_security_group_ip_range

AwsRdsDbSecurityGroupIpRanges: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_security_group_ip_range.AwsRdsDbSecurityGroupIpRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSecurityGroupIpRanges) -> list:
    import capo_securityhub.types.aws_rds_db_security_group_ip_range

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_security_group_ip_range.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbSecurityGroupIpRanges:
    import capo_securityhub.types.aws_rds_db_security_group_ip_range

    out: AwsRdsDbSecurityGroupIpRanges = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_security_group_ip_range.deserialize_json(
                item
            )
        )
    return out
