"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DaemonNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class DaemonNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#DaemonNotFoundException``."""

    code: str | None = "DaemonNotFoundException"

    def __init__(self, data: DaemonNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DaemonNotFoundException",
        )
        self.data = data
