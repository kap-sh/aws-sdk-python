"""Generated from Smithy shape ``com.amazonaws.ecs#UnsupportedFeatureException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class UnsupportedFeatureException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class UnsupportedFeatureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#UnsupportedFeatureException``."""

    code: str | None = "UnsupportedFeatureException"

    def __init__(self, data: UnsupportedFeatureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedFeatureException",
        )
        self.data = data
