"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn


class DescribeBackupInput(TypedDict):
    backup_arn: "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    """<p>The Amazon Resource Name (ARN) associated with the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBackupInput) -> dict:
    out: dict = {}
    out["BackupArn"] = value["backup_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBackupInput:
    out: DescribeBackupInput = {}  # type: ignore[typeddict-item]
    if "BackupArn" in data:
        out["backup_arn"] = data["BackupArn"]
    else:
        raise DeserializationError("DescribeBackupInput.backup_arn required")
    return out
