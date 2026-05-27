"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.item_response

ItemResponseList: TypeAlias = list["aws_sdk_dynamodb.types.item_response.ItemResponse"]
