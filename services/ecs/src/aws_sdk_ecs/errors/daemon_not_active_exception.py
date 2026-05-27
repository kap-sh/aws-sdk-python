"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonNotActiveException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DaemonNotActiveException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class DaemonNotActiveException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#DaemonNotActiveException``."""

    code: str | None = "DaemonNotActiveException"

    def __init__(self, data: DaemonNotActiveException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DaemonNotActiveException",
        )
        self.data = data
