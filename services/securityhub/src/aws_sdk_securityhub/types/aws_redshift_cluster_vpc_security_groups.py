"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterVpcSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_group

AwsRedshiftClusterVpcSecurityGroups: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_group.AwsRedshiftClusterVpcSecurityGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterVpcSecurityGroups) -> list:
    import aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterVpcSecurityGroups:
    import aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_group

    out: AwsRedshiftClusterVpcSecurityGroups = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_redshift_cluster_vpc_security_group.deserialize_json(
                item
            )
        )
    return out
