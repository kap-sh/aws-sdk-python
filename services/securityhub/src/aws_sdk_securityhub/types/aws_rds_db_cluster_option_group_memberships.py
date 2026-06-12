"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterOptionGroupMemberships``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_option_group_membership

AwsRdsDbClusterOptionGroupMemberships: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_cluster_option_group_membership.AwsRdsDbClusterOptionGroupMembership"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterOptionGroupMemberships) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_option_group_membership

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_cluster_option_group_membership.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbClusterOptionGroupMemberships:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_option_group_membership

    out: AwsRdsDbClusterOptionGroupMemberships = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_cluster_option_group_membership.deserialize_json(
                item
            )
        )
    return out
