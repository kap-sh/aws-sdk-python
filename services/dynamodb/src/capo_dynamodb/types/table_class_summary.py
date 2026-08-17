"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableClassSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.date
    import capo_dynamodb.types.table_class


class TableClassSummary(TypedDict, closed=True):
    table_class: NotRequired["capo_dynamodb.types.table_class.TableClass"]
    """<p>The table class of the specified table. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</p>"""
    last_update_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>The date and time at which the table class was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableClassSummary) -> dict:
    out: dict = {}
    if "table_class" in value:
        import capo_dynamodb.types.table_class

        out["TableClass"] = capo_dynamodb.types.table_class.serialize_aws_json_1_0(
            value["table_class"]
        )
    if "last_update_date_time" in value:
        import capo_dynamodb.types.date

        out["LastUpdateDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
            value["last_update_date_time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableClassSummary:
    out: TableClassSummary = {}  # type: ignore[typeddict-item]
    if data.get("TableClass") is not None:
        import capo_dynamodb.types.table_class

        out["table_class"] = capo_dynamodb.types.table_class.deserialize_aws_json_1_0(
            data["TableClass"]
        )
    if data.get("LastUpdateDateTime") is not None:
        import capo_dynamodb.types.date

        out["last_update_date_time"] = (
            capo_dynamodb.types.date.deserialize_aws_json_1_0(
                data["LastUpdateDateTime"]
            )
        )
    return out
