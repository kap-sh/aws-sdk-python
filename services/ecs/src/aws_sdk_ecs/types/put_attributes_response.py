"""Generated from Smithy shape ``com.amazonaws.ecs#PutAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes


class PutAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>The attributes applied to your resource.</p>"""
