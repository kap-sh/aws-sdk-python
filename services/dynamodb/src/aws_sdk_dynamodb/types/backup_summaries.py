"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_summary

BackupSummaries: TypeAlias = list["aws_sdk_dynamodb.types.backup_summary.BackupSummary"]
