"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_summary

ExportSummaries: TypeAlias = list["aws_sdk_dynamodb.types.export_summary.ExportSummary"]
