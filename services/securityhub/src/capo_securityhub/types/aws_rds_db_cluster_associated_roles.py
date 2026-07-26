"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterAssociatedRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_cluster_associated_role

AwsRdsDbClusterAssociatedRoles: TypeAlias = list[
    "capo_securityhub.types.aws_rds_db_cluster_associated_role.AwsRdsDbClusterAssociatedRole"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterAssociatedRoles) -> list:
    import capo_securityhub.types.aws_rds_db_cluster_associated_role

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_rds_db_cluster_associated_role.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbClusterAssociatedRoles:
    import capo_securityhub.types.aws_rds_db_cluster_associated_role

    out: AwsRdsDbClusterAssociatedRoles = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_rds_db_cluster_associated_role.deserialize_json(
                item
            )
        )
    return out
