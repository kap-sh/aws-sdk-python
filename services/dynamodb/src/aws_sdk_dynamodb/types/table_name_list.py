"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_name

TableNameList: TypeAlias = list["aws_sdk_dynamodb.types.table_name.TableName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TableNameList:
    return list(data)
