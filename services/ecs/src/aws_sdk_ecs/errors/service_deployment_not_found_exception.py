"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceDeploymentNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class ServiceDeploymentNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ServiceDeploymentNotFoundException``."""

    code: str | None = "ServiceDeploymentNotFoundException"

    def __init__(self, data: ServiceDeploymentNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceDeploymentNotFoundException",
        )
        self.data = data
