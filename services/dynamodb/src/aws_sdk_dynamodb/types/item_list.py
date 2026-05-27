"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map

ItemList: TypeAlias = list["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
