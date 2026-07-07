"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudhsm_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup_retention_policy
    import aws_sdk_cloudhsm_v2.types.cluster_id
    import aws_sdk_cloudhsm_v2.types.hsm_type


class ModifyClusterRequest(TypedDict, closed=True):
    hsm_type: NotRequired["aws_sdk_cloudhsm_v2.types.hsm_type.HsmType"]
    """<p>The desired HSM type of the cluster.</p>"""
    backup_retention_policy: NotRequired[
        "aws_sdk_cloudhsm_v2.types.backup_retention_policy.BackupRetentionPolicy"
    ]
    """<p>A policy that defines how the service retains backups.</p>"""
    cluster_id: "aws_sdk_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the cluster that you want to modify. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClusterRequest) -> dict:
    out: dict = {}
    if "hsm_type" in value:
        out["HsmType"] = value["hsm_type"]
    if "backup_retention_policy" in value:
        import aws_sdk_cloudhsm_v2.types.backup_retention_policy

        out["BackupRetentionPolicy"] = (
            aws_sdk_cloudhsm_v2.types.backup_retention_policy.serialize_aws_json_1_1(
                value["backup_retention_policy"]
            )
        )
    out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClusterRequest:
    out: ModifyClusterRequest = {}  # type: ignore[typeddict-item]
    if "HsmType" in data:
        out["hsm_type"] = data["HsmType"]
    if "BackupRetentionPolicy" in data:
        import aws_sdk_cloudhsm_v2.types.backup_retention_policy

        out["backup_retention_policy"] = (
            aws_sdk_cloudhsm_v2.types.backup_retention_policy.deserialize_aws_json_1_1(
                data["BackupRetentionPolicy"]
            )
        )
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    else:
        raise DeserializationError("ModifyClusterRequest.cluster_id required")
    return out
