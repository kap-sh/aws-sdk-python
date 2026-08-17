"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.backup_summary

BackupSummaries: TypeAlias = list["capo_dynamodb.types.backup_summary.BackupSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupSummaries) -> list:
    import capo_dynamodb.types.backup_summary

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.backup_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BackupSummaries:
    import capo_dynamodb.types.backup_summary

    out: BackupSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.backup_summary.deserialize_aws_json_1_0(item))
    return out
