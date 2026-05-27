"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.transact_get_item

TransactGetItemList: TypeAlias = list[
    "aws_sdk_dynamodb.types.transact_get_item.TransactGetItem"
]
