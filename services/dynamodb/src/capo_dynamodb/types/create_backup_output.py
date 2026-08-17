"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_details


class CreateBackupOutput(TypedDict, closed=True):
    backup_details: NotRequired["capo_dynamodb.types.backup_details.BackupDetails"]
    """<p>Contains the details of the backup created for the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBackupOutput) -> dict:
    out: dict = {}
    if "backup_details" in value:
        import capo_dynamodb.types.backup_details

        out["BackupDetails"] = (
            capo_dynamodb.types.backup_details.serialize_aws_json_1_0(
                value["backup_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBackupOutput:
    out: CreateBackupOutput = {}  # type: ignore[typeddict-item]
    if data.get("BackupDetails") is not None:
        import capo_dynamodb.types.backup_details

        out["backup_details"] = (
            capo_dynamodb.types.backup_details.deserialize_aws_json_1_0(
                data["BackupDetails"]
            )
        )
    return out
