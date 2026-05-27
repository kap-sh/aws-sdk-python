"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service


class DeleteServiceResponse(TypedDict):
    service: NotRequired["aws_sdk_ecs.types.service.Service"]
    """<p>The full description of the deleted service.</p>"""
