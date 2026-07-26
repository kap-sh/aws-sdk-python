"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbOptionGroupMemberships``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_option_group_membership

AwsRdsDbOptionGroupMemberships: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_option_group_membership.AwsRdsDbOptionGroupMembership"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbOptionGroupMemberships) -> list:
    import capo_securityhub.types.aws_rds_db_option_group_membership

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_option_group_membership.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbOptionGroupMemberships:
    import capo_securityhub.types.aws_rds_db_option_group_membership

    out: AwsRdsDbOptionGroupMemberships = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_option_group_membership.deserialize_json(
                item
            )
        )
    return out
