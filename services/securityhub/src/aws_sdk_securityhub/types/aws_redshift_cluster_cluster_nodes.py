"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_node

AwsRedshiftClusterClusterNodes: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_redshift_cluster_cluster_node.AwsRedshiftClusterClusterNode"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterNodes) -> list:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_node

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_node.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterClusterNodes:
    import aws_sdk_securityhub.types.aws_redshift_cluster_cluster_node

    out: AwsRedshiftClusterClusterNodes = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_redshift_cluster_cluster_node.deserialize_json(
                item
            )
        )
    return out
