"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ClusterNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class ClusterNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ClusterNotFoundException``."""

    code: str | None = "ClusterNotFoundException"

    def __init__(self, data: ClusterNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterNotFoundException",
        )
        self.data = data
