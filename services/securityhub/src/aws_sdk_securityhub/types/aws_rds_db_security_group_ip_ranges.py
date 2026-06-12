"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSecurityGroupIpRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_security_group_ip_range

AwsRdsDbSecurityGroupIpRanges: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_security_group_ip_range.AwsRdsDbSecurityGroupIpRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSecurityGroupIpRanges) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_security_group_ip_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_security_group_ip_range.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbSecurityGroupIpRanges:
    import aws_sdk_securityhub.types.aws_rds_db_security_group_ip_range

    out: AwsRdsDbSecurityGroupIpRanges = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_security_group_ip_range.deserialize_json(
                item
            )
        )
    return out
