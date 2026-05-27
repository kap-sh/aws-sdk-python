"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeExportInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_arn


class DescribeExportInput(TypedDict):
    export_arn: "aws_sdk_dynamodb.types.export_arn.ExportArn"
    """<p>The Amazon Resource Name (ARN) associated with the export.</p>"""
