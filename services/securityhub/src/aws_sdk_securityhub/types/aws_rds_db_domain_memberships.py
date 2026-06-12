"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbDomainMemberships``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_domain_membership

AwsRdsDbDomainMemberships: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_domain_membership.AwsRdsDbDomainMembership"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbDomainMemberships) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_domain_membership

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_domain_membership.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbDomainMemberships:
    import aws_sdk_securityhub.types.aws_rds_db_domain_membership

    out: AwsRdsDbDomainMemberships = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_domain_membership.deserialize_json(
                item
            )
        )
    return out
