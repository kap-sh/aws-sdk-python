"""Generated from Smithy shape ``com.amazonaws.ecs#NoUpdateAvailableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class NoUpdateAvailableException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class NoUpdateAvailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#NoUpdateAvailableException``."""

    code: str | None = "NoUpdateAvailableException"

    def __init__(self, data: NoUpdateAvailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoUpdateAvailableException",
        )
        self.data = data
