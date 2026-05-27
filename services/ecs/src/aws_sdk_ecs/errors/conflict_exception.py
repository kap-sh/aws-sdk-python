"""Generated from Smithy shape ``com.amazonaws.ecs#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.resource_ids
    import aws_sdk_ecs.types.string


class ConflictException_(TypedDict):
    resource_ids: NotRequired["aws_sdk_ecs.types.resource_ids.ResourceIds"]
    """<p>The existing task ARNs which are already associated with the <code>clientToken</code>.</p>"""
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data
