"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeImportInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.import_arn


class DescribeImportInput(TypedDict):
    import_arn: "aws_sdk_dynamodb.types.import_arn.ImportArn"
    """<p> The Amazon Resource Name (ARN) associated with the table you're importing to. </p>"""
