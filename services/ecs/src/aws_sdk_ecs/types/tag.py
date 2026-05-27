"""Generated from Smithy shape ``com.amazonaws.ecs#Tag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.tag_key
    import aws_sdk_ecs.types.tag_value


class Tag(TypedDict):
    key: NotRequired["aws_sdk_ecs.types.tag_key.TagKey"]
    """<p>One part of a key-value pair that make up a tag. A <code>key</code> is a general label that acts like a category for more specific tag values.</p>"""
    value: NotRequired["aws_sdk_ecs.types.tag_value.TagValue"]
    """<p>The optional part of a key-value pair that make up a tag. A <code>value</code> acts as a descriptor within a tag category (key).</p>"""
