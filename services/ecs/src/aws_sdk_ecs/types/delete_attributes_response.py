"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes


class DeleteAttributesResponse(TypedDict):
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>A list of attribute objects that were successfully deleted from your resource.</p>"""
