"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.transact_write_item

TransactWriteItemList: TypeAlias = list[
    "aws_sdk_dynamodb.types.transact_write_item.TransactWriteItem"
]
