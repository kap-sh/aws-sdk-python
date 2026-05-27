"""Generated from Smithy shape ``com.amazonaws.ecs#ServerException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServerException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class ServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ServerException``."""

    code: str | None = "ServerException"

    def __init__(self, data: ServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerException",
        )
        self.data = data
