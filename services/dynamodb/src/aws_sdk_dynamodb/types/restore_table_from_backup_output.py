"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableFromBackupOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_description


class RestoreTableFromBackupOutput(TypedDict):
    table_description: NotRequired[
        "aws_sdk_dynamodb.types.table_description.TableDescription"
    ]
    """<p>The description of the table created from an existing backup.</p>"""
