"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateBackupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_name
    import capo_dynamodb.types.table_arn


class CreateBackupInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    backup_name: "capo_dynamodb.types.backup_name.BackupName"
    """<p>Specified name for the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBackupInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["BackupName"] = value["backup_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBackupInput:
    out: CreateBackupInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("CreateBackupInput.table_name required")
    if "BackupName" in data:
        out["backup_name"] = data["BackupName"]
    else:
        raise DeserializationError("CreateBackupInput.backup_name required")
    return out
