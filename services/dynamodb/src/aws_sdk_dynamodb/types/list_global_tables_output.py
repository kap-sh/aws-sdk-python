"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListGlobalTablesOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table_list
    import aws_sdk_dynamodb.types.table_name


class ListGlobalTablesOutput(TypedDict):
    global_tables: NotRequired[
        "aws_sdk_dynamodb.types.global_table_list.GlobalTableList"
    ]
    """<p>List of global table names.</p>"""
    last_evaluated_global_table_name: NotRequired[
        "aws_sdk_dynamodb.types.table_name.TableName"
    ]
    """<p>Last evaluated global table name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListGlobalTablesOutput) -> dict:
    out: dict = {}
    if "global_tables" in value:
        import aws_sdk_dynamodb.types.global_table_list

        out["GlobalTables"] = (
            aws_sdk_dynamodb.types.global_table_list.serialize_aws_json_1_0(
                value["global_tables"]
            )
        )
    if "last_evaluated_global_table_name" in value:
        out["LastEvaluatedGlobalTableName"] = value["last_evaluated_global_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListGlobalTablesOutput:
    out: ListGlobalTablesOutput = {}  # type: ignore[typeddict-item]
    if "GlobalTables" in data:
        import aws_sdk_dynamodb.types.global_table_list

        out["global_tables"] = (
            aws_sdk_dynamodb.types.global_table_list.deserialize_aws_json_1_0(
                data["GlobalTables"]
            )
        )
    if "LastEvaluatedGlobalTableName" in data:
        out["last_evaluated_global_table_name"] = data["LastEvaluatedGlobalTableName"]
    return out
