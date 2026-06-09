"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateBackupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_details


class CreateBackupOutput(TypedDict):
    backup_details: NotRequired["aws_sdk_dynamodb.types.backup_details.BackupDetails"]
    """<p>Contains the details of the backup created for the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBackupOutput) -> dict:
    out: dict = {}
    if "backup_details" in value:
        import aws_sdk_dynamodb.types.backup_details

        out["BackupDetails"] = (
            aws_sdk_dynamodb.types.backup_details.serialize_aws_json_1_0(
                value["backup_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBackupOutput:
    out: CreateBackupOutput = {}  # type: ignore[typeddict-item]
    if "BackupDetails" in data:
        import aws_sdk_dynamodb.types.backup_details

        out["backup_details"] = (
            aws_sdk_dynamodb.types.backup_details.deserialize_aws_json_1_0(
                data["BackupDetails"]
            )
        )
    return out
