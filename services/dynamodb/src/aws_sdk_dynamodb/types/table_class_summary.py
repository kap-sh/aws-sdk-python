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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableClassSummary) -> dict:
    out: dict = {}
    if "table_class" in value:
        import aws_sdk_dynamodb.types.table_class

        out["TableClass"] = aws_sdk_dynamodb.types.table_class.serialize_aws_json_1_0(
            value["table_class"]
        )
    if "last_update_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["LastUpdateDateTime"] = aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
            value["last_update_date_time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableClassSummary:
    out: TableClassSummary = {}  # type: ignore[typeddict-item]
    if "TableClass" in data:
        import aws_sdk_dynamodb.types.table_class

        out["table_class"] = (
            aws_sdk_dynamodb.types.table_class.deserialize_aws_json_1_0(
                data["TableClass"]
            )
        )
    if "LastUpdateDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["last_update_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["LastUpdateDateTime"]
            )
        )
    return out
