"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_cluster_security_group

AwsRedshiftClusterClusterSecurityGroups: TypeAlias = list[
    "capo_securityhub.types.aws_redshift_cluster_cluster_security_group.AwsRedshiftClusterClusterSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterSecurityGroups) -> list:
    import capo_securityhub.types.aws_redshift_cluster_cluster_security_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_cluster_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterClusterSecurityGroups:
    import capo_securityhub.types.aws_redshift_cluster_cluster_security_group

    out: AwsRedshiftClusterClusterSecurityGroups = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_cluster_security_group.deserialize_json(
                item
            )
        )
    return out
