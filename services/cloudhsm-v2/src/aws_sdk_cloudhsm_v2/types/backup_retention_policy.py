"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupRetentionPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.backup_retention_type
    import aws_sdk_cloudhsm_v2.types.backup_retention_value


class BackupRetentionPolicy(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_cloudhsm_v2.types.backup_retention_type.BackupRetentionType"
    ]
    """<p>The type of backup retention policy. For the <code>DAYS</code> type, the value is the number of days to retain backups.</p>"""
    value: NotRequired[
        "aws_sdk_cloudhsm_v2.types.backup_retention_value.BackupRetentionValue"
    ]
    """<p>Use a value between 7 - 379.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupRetentionPolicy) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_cloudhsm_v2.types.backup_retention_type

        out["Type"] = (
            aws_sdk_cloudhsm_v2.types.backup_retention_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackupRetentionPolicy:
    out: BackupRetentionPolicy = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_cloudhsm_v2.types.backup_retention_type

        out["type"] = (
            aws_sdk_cloudhsm_v2.types.backup_retention_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
