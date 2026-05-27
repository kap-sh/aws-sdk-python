"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class ServiceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ServiceNotFoundException``."""

    code: str | None = "ServiceNotFoundException"

    def __init__(self, data: ServiceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceNotFoundException",
        )
        self.data = data
