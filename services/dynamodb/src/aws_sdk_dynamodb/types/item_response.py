"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_map


class ItemResponse(TypedDict):
    item: NotRequired["aws_sdk_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Map of attribute data consisting of the data type and attribute value.</p>"""
