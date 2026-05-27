"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreTableToPointInTimeOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_description


class RestoreTableToPointInTimeOutput(TypedDict):
    table_description: NotRequired[
        "aws_sdk_dynamodb.types.table_description.TableDescription"
    ]
    """<p>Represents the properties of a table.</p>"""
