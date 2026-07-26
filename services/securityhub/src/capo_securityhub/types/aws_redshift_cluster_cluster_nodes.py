"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterClusterNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_cluster_node

AwsRedshiftClusterClusterNodes: TypeAlias = list[
    "capo_securityhub.types.aws_redshift_cluster_cluster_node.AwsRedshiftClusterClusterNode"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterClusterNodes) -> list:
    import capo_securityhub.types.aws_redshift_cluster_cluster_node

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_cluster_node.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterClusterNodes:
    import capo_securityhub.types.aws_redshift_cluster_cluster_node

    out: AwsRedshiftClusterClusterNodes = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_cluster_node.deserialize_json(
                item
            )
        )
    return out
