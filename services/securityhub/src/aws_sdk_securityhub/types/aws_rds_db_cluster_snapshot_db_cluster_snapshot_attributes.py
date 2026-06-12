"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbClusterSnapshotDbClusterSnapshotAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute

AwsRdsDbClusterSnapshotDbClusterSnapshotAttributes: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute.AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbClusterSnapshotDbClusterSnapshotAttributes) -> list:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRdsDbClusterSnapshotDbClusterSnapshotAttributes:
    import aws_sdk_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute

    out: AwsRdsDbClusterSnapshotDbClusterSnapshotAttributes = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_rds_db_cluster_snapshot_db_cluster_snapshot_attribute.deserialize_json(
                item
            )
        )
    return out
