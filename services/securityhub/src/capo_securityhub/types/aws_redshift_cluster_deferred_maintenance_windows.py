"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterDeferredMaintenanceWindows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_redshift_cluster_deferred_maintenance_window

AwsRedshiftClusterDeferredMaintenanceWindows: TypeAlias = list[
    "capo_securityhub.types.aws_redshift_cluster_deferred_maintenance_window.AwsRedshiftClusterDeferredMaintenanceWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterDeferredMaintenanceWindows) -> list:
    import capo_securityhub.types.aws_redshift_cluster_deferred_maintenance_window

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_deferred_maintenance_window.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRedshiftClusterDeferredMaintenanceWindows:
    import capo_securityhub.types.aws_redshift_cluster_deferred_maintenance_window

    out: AwsRedshiftClusterDeferredMaintenanceWindows = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_redshift_cluster_deferred_maintenance_window.deserialize_json(
                item
            )
        )
    return out
