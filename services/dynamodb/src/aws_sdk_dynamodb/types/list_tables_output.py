"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTablesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_name
    import aws_sdk_dynamodb.types.table_name_list


class ListTablesOutput(TypedDict, closed=True):
    table_names: NotRequired["aws_sdk_dynamodb.types.table_name_list.TableNameList"]
    """<p>The names of the tables associated with the current account at the current endpoint. The maximum size of this array is 100.</p> <p>If <code>LastEvaluatedTableName</code> also appears in the output, you can use this value as the <code>ExclusiveStartTableName</code> parameter in a subsequent <code>ListTables</code> request and obtain the next page of results.</p>"""
    last_evaluated_table_name: NotRequired[
        "aws_sdk_dynamodb.types.table_name.TableName"
    ]
    """<p>The name of the last table in the current page of results. Use this value as the <code>ExclusiveStartTableName</code> in a new request to obtain the next page of results, until all the table names are returned.</p> <p>If you do not receive a <code>LastEvaluatedTableName</code> value in the response, this means that there are no more table names to be retrieved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTablesOutput) -> dict:
    out: dict = {}
    if "table_names" in value:
        import aws_sdk_dynamodb.types.table_name_list

        out["TableNames"] = (
            aws_sdk_dynamodb.types.table_name_list.serialize_aws_json_1_0(
                value["table_names"]
            )
        )
    if "last_evaluated_table_name" in value:
        out["LastEvaluatedTableName"] = value["last_evaluated_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTablesOutput:
    out: ListTablesOutput = {}  # type: ignore[typeddict-item]
    if "TableNames" in data:
        import aws_sdk_dynamodb.types.table_name_list

        out["table_names"] = (
            aws_sdk_dynamodb.types.table_name_list.deserialize_aws_json_1_0(
                data["TableNames"]
            )
        )
    if "LastEvaluatedTableName" in data:
        out["last_evaluated_table_name"] = data["LastEvaluatedTableName"]
    return out
