"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RdsDbSnapshotConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_attributes_map
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_kms_key_id


class RdsDbSnapshotConfiguration(TypedDict):
    attributes: NotRequired[
        "aws_sdk_accessanalyzer.types.rds_db_snapshot_attributes_map.RdsDbSnapshotAttributesMap"
    ]
    """<p>The names and values of manual DB snapshot attributes. Manual DB snapshot attributes are used to authorize other Amazon Web Services accounts to restore a manual DB snapshot. The only valid value for <code>attributeName</code> for the attribute map is restore.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_accessanalyzer.types.rds_db_snapshot_kms_key_id.RdsDbSnapshotKmsKeyId"
    ]
    """<p>The KMS key identifier for an encrypted Amazon RDS DB snapshot. The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p> <ul> <li> <p>If the configuration is for an existing Amazon RDS DB snapshot and you do not specify the <code>kmsKeyId</code>, or you specify an empty string, then the access preview uses the existing <code>kmsKeyId</code> of the snapshot.</p> </li> <li> <p>If the access preview is for a new resource and you do not specify the specify the <code>kmsKeyId</code>, then the access preview considers the snapshot as unencrypted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbSnapshotConfiguration) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_attributes_map

        out["attributes"] = (
            aws_sdk_accessanalyzer.types.rds_db_snapshot_attributes_map.serialize_json(
                value["attributes"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> RdsDbSnapshotConfiguration:
    out: RdsDbSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_attributes_map

        out["attributes"] = (
            aws_sdk_accessanalyzer.types.rds_db_snapshot_attributes_map.deserialize_json(
                data["attributes"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
