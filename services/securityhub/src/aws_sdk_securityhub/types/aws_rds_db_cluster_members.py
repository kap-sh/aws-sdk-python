"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_member

AwsRdsDbClusterMembers: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_cluster_member.AwsRdsDbClusterMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterMembers) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_cluster_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbClusterMembers:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_member

    out: AwsRdsDbClusterMembers = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_cluster_member.deserialize_json(item)
        )
    return out
