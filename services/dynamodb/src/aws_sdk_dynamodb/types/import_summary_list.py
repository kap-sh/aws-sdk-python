"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_summary

ImportSummaryList: TypeAlias = list[
    "aws_sdk_dynamodb.types.import_summary.ImportSummary"
]
