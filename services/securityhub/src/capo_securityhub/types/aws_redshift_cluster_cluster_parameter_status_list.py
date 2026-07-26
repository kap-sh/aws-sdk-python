"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterParameterStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status

AwsRedshiftClusterClusterParameterStatusList: TypeAlias = list[
    "capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status.AwsRedshiftClusterClusterParameterStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterParameterStatusList) -> list:
    import capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterClusterParameterStatusList:
    import capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status

    out: AwsRedshiftClusterClusterParameterStatusList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_cluster_parameter_status.deserialize_json(
                item
            )
        )
    return out
