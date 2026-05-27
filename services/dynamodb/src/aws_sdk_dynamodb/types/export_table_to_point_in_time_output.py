"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportTableToPointInTimeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.export_description


class ExportTableToPointInTimeOutput(TypedDict):
    export_description: NotRequired[
        "aws_sdk_dynamodb.types.export_description.ExportDescription"
    ]
    """<p>Contains a description of the table export.</p>"""
