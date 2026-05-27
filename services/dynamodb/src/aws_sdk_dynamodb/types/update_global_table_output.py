"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_description


class UpdateGlobalTableOutput(TypedDict):
    global_table_description: NotRequired[
        "aws_sdk_dynamodb.types.global_table_description.GlobalTableDescription"
    ]
    """<p>Contains the details of the global table.</p>"""
