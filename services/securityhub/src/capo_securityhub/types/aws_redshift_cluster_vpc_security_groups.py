"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterVpcSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_vpc_security_group

AwsRedshiftClusterVpcSecurityGroups: TypeAlias = list[
    "capo_securityhub.types.aws_redshift_cluster_vpc_security_group.AwsRedshiftClusterVpcSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterVpcSecurityGroups) -> list:
    import capo_securityhub.types.aws_redshift_cluster_vpc_security_group

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_vpc_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterVpcSecurityGroups:
    import capo_securityhub.types.aws_redshift_cluster_vpc_security_group

    out: AwsRedshiftClusterVpcSecurityGroups = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_vpc_security_group.deserialize_json(
                item
            )
        )
    return out
