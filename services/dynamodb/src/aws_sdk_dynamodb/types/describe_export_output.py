"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeExportOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_description


class DescribeExportOutput(TypedDict):
    export_description: NotRequired[
        "aws_sdk_dynamodb.types.export_description.ExportDescription"
    ]
    """<p>Represents the properties of the export.</p>"""
