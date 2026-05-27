"""Generated from Smithy shape ``com.amazonaws.ecs#CreatedAt``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.timestamp


class CreatedAt(TypedDict):
    before: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>Include service deployments in the result that were created before this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    after: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>Include service deployments in the result that were created after this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
