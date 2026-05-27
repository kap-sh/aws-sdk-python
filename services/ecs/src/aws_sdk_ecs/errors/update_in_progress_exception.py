"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateInProgressException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class UpdateInProgressException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class UpdateInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#UpdateInProgressException``."""

    code: str | None = "UpdateInProgressException"

    def __init__(self, data: UpdateInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UpdateInProgressException",
        )
        self.data = data
