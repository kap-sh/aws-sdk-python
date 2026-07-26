"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbClusterSnapshotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.rds_db_cluster_snapshot_attributes_map
    import capo_accessanalyzer.types.rds_db_cluster_snapshot_kms_key_id


class RdsDbClusterSnapshotConfiguration(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_accessanalyzer.types.rds_db_cluster_snapshot_attributes_map.RdsDbClusterSnapshotAttributesMap"
    ]
    """<p>The names and values of manual DB cluster snapshot attributes. Manual DB cluster snapshot attributes are used to authorize other Amazon Web Services accounts to restore a manual DB cluster snapshot. The only valid value for <code>AttributeName</code> for the attribute map is <code>restore</code> </p>"""
    kms_key_id: NotRequired[
        "capo_accessanalyzer.types.rds_db_cluster_snapshot_kms_key_id.RdsDbClusterSnapshotKmsKeyId"
    ]
    """<p>The KMS key identifier for an encrypted Amazon RDS DB cluster snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <ul> <li> <p>If the configuration is for an existing Amazon RDS DB cluster snapshot and you do not specify the <code>kmsKeyId</code>, or you specify an empty string, then the access preview uses the existing <code>kmsKeyId</code> of the snapshot.</p> </li> <li> <p>If the access preview is for a new resource and you do not specify the specify the <code>kmsKeyId</code>, then the access preview considers the snapshot as unencrypted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbClusterSnapshotConfiguration) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_accessanalyzer.types.rds_db_cluster_snapshot_attributes_map

        out["attributes"] = (
            capo_accessanalyzer.types.rds_db_cluster_snapshot_attributes_map.serialize_json(
                value["attributes"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> RdsDbClusterSnapshotConfiguration:
    out: RdsDbClusterSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import capo_accessanalyzer.types.rds_db_cluster_snapshot_attributes_map

        out["attributes"] = (
            capo_accessanalyzer.types.rds_db_cluster_snapshot_attributes_map.deserialize_json(
                data["attributes"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
