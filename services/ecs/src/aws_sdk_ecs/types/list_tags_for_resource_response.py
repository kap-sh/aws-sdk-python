"""Generated from Smithy shape ``com.amazonaws.ecs#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The tags for the resource.</p>"""
