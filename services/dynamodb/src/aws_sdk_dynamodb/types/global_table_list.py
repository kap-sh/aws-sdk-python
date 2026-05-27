"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.global_table

GlobalTableList: TypeAlias = list["aws_sdk_dynamodb.types.global_table.GlobalTable"]
