"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_description


class DescribeBackupOutput(TypedDict, closed=True):
    backup_description: NotRequired[
        "aws_sdk_dynamodb.types.backup_description.BackupDescription"
    ]
    """<p>Contains the description of the backup created for the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBackupOutput) -> dict:
    out: dict = {}
    if "backup_description" in value:
        import aws_sdk_dynamodb.types.backup_description

        out["BackupDescription"] = (
            aws_sdk_dynamodb.types.backup_description.serialize_aws_json_1_0(
                value["backup_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBackupOutput:
    out: DescribeBackupOutput = {}  # type: ignore[typeddict-item]
    if "BackupDescription" in data:
        import aws_sdk_dynamodb.types.backup_description

        out["backup_description"] = (
            aws_sdk_dynamodb.types.backup_description.deserialize_aws_json_1_0(
                data["BackupDescription"]
            )
        )
    return out
