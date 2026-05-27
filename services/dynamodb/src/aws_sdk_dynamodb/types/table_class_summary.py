"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableClassSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.table_class


class TableClassSummary(TypedDict):
    table_class: NotRequired["aws_sdk_dynamodb.types.table_class.TableClass"]
    """<p>The table class of the specified table. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</p>"""
    last_update_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The date and time at which the table class was last updated.</p>"""
