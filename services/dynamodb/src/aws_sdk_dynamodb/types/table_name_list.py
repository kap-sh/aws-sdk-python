"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.table_name

TableNameList: TypeAlias = list["aws_sdk_dynamodb.types.table_name.TableName"]
