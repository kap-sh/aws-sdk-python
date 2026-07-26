"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbDomainMemberships``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_domain_membership

AwsRdsDbDomainMemberships: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_domain_membership.AwsRdsDbDomainMembership"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbDomainMemberships) -> list:
    import capo_securityhub.types.aws_rds_db_domain_membership

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_domain_membership.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbDomainMemberships:
    import capo_securityhub.types.aws_rds_db_domain_membership

    out: AwsRdsDbDomainMemberships = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_domain_membership.deserialize_json(item)
        )
    return out
