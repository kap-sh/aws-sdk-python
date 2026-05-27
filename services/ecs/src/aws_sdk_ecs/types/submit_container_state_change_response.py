"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitContainerStateChangeResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class SubmitContainerStateChangeResponse(TypedDict):
    acknowledgment: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Acknowledgement of the state change.</p>"""
