"""Generated from Smithy shape ``com.amazonaws.ecs#MissingVersionException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class MissingVersionException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class MissingVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#MissingVersionException``."""

    code: str | None = "MissingVersionException"

    def __init__(self, data: MissingVersionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingVersionException",
        )
        self.data = data
