"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteBackupInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn


class DeleteBackupInput(TypedDict):
    backup_arn: "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    """<p>The ARN associated with the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBackupInput) -> dict:
    out: dict = {}
    out["BackupArn"] = value["backup_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBackupInput:
    out: DeleteBackupInput = {}  # type: ignore[typeddict-item]
    if "BackupArn" in data:
        out["backup_arn"] = data["BackupArn"]
    else:
        raise DeserializationError("DeleteBackupInput.backup_arn required")
    return out
