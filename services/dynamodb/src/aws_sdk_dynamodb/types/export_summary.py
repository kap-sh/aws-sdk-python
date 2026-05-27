"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_arn
    import aws_sdk_dynamodb.types.export_status
    import aws_sdk_dynamodb.types.export_type


class ExportSummary(TypedDict):
    export_arn: NotRequired["aws_sdk_dynamodb.types.export_arn.ExportArn"]
    """<p>The Amazon Resource Name (ARN) of the export.</p>"""
    export_status: NotRequired["aws_sdk_dynamodb.types.export_status.ExportStatus"]
    """<p>Export can be in one of the following states: IN_PROGRESS, COMPLETED, or FAILED.</p>"""
    export_type: NotRequired["aws_sdk_dynamodb.types.export_type.ExportType"]
    """<p>The type of export that was performed. Valid values are <code>FULL_EXPORT</code> or <code>INCREMENTAL_EXPORT</code>.</p>"""
