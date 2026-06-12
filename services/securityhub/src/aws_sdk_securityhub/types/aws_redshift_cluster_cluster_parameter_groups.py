"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterParameterGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_group

AwsRedshiftClusterClusterParameterGroups: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_group.AwsRedshiftClusterClusterParameterGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterParameterGroups) -> list:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterClusterParameterGroups:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_group

    out: AwsRedshiftClusterClusterParameterGroups = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_parameter_group.deserialize_json(
                item
            )
        )
    return out
